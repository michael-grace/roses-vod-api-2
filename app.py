from aiohttp import web
import aiohttp_cors

import json
import typing as T
import time

import config


vods: T.List[T.Dict[str, T.Union[str, int]]] = []


def writeback():
    with open("data.json", "w") as f:
        f.write(json.dumps(vods))


async def get_all_vods(_: web.Request) -> web.Response:
    return web.json_response({
        "vods": vods
    })


async def add_vod(req: web.Request) -> web.Response:
    data: T.Dict[str, str] = await req.json()
    for part in ["title", "description", "url"]:
        if part not in data:
            raise web.HTTPBadRequest

    global vods

    new_vod = {
        "id": int(time.time()),
        "title": data["title"],
        "description": data["description"],
        "url": data["url"]
    }

    vods.append(new_vod)

    writeback()

    return web.json_response(new_vod)


async def update_vod(req: web.Request) -> web.Response:
    data: T.Dict[str, str] = await req.json()
    for part in ["title", "description", "url"]:
        if part not in data:
            raise web.HTTPBadRequest

    try:
        id = int(req.match_info["id"])
    except (ValueError, KeyError):
        raise web.HTTPBadRequest

    global vods

    # Check ID Exists
    for vod in vods:
        if vod["id"] == id:
            break
    else:
        raise web.HTTPNotFound

    updated_vod = {
        "id": id,
        "title": data["title"],
        "description": data["description"],
        "url": data["url"]
    }

    vods = [x if x["id"] != id
            else updated_vod for x in vods]

    writeback()

    return web.json_response(updated_vod)


async def delete_vod(req: web.Request) -> web.Response:
    try:
        id = int(req.match_info["id"])
    except (ValueError, KeyError):
        raise web.HTTPBadRequest

    global vods

    # Check ID Exists
    for vod in vods:
        if vod["id"] == id:
            break
    else:
        raise web.HTTPNotFound

    print(f"Deleting VOD ID: {id}")
    vods = [x for x in vods if x["id"] != id]

    writeback()

    return web.json_response({
        "Deleted": id
    })


async def manage_redirect(_: web.Request) -> web.Response:
    raise web.HTTPFound("/manage/index.html")

with open("data.json") as f:
    vods = json.load(f)

app = web.Application()
cors = aiohttp_cors.setup(app)

# CORS
cors.add(app.router.add_get("/all_vods", get_all_vods), {  # type: ignore
    "https://roseslive.co.uk": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        allow_headers="*",
        allow_methods="*"
    )
})

app.add_routes([
    web.post("/vod", add_vod),
    web.put("/vod/{id}", update_vod),
    web.delete("/vod/{id}", delete_vod),

    web.get("/manage", manage_redirect),
    web.static("/manage", "views")
])

print("Starting Server")
web.run_app(app, port=config.PORT)
