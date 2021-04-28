from aiohttp import web
import aiohttp_cors
import json
import typing as T
import random
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
        "id": random.randint(0, 1000000), # Lets hope theres no conflicts
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
  


with open("data.json") as f:
    vods = json.load(f)

app = web.Application()
cors = aiohttp_cors.setup(app)

cors.add(app.router.add_get("/all_vods", get_all_vods), { #type: ignore
    "https://roseslive.co.uk": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        allow_headers="*",
        allow_methods="*"
    )
})

app.add_routes([
    web.post("/vod", add_vod),
    web.patch("/vod/{id}", update_vod)
])

print("Starting Server")
web.run_app(app, port=config.PORT)