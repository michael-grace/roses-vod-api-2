var main_data;

const edit = (id) => {
    // Find the VOD
    var vod_to_update;
    main_data.vods.forEach(element => {
        if (element.id === id) {
            vod_to_update = element;
        }
    })

    document.getElementById("vod-title").value = vod_to_update.title;
    document.getElementById("vod-description").value = vod_to_update.description;
    document.getElementById("vod-url").value = vod_to_update.url;

    // Send Update
    document.getElementById("vod-submit").onclick = () => {
        fetch(`/vod/${id}`,
            {
                method: "put",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    "title": document.getElementById("vod-title").value,
                    "description": document.getElementById("vod-description").value,
                    "url": document.getElementById("vod-url").value,
                })
            }).then(() => { window.location.reload() });
    }
}

const addVod = () => {
    document.getElementById("vod-submit").onclick = () => {
        fetch("/vod",
            {
                method: "post",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    "title": document.getElementById("vod-title").value,
                    "description": document.getElementById("vod-description").value,
                    "url": document.getElementById("vod-url").value,
                })
            }).then(() => { window.location.reload() });
    }
}

const deleteVod = (id) => {
    // Find the VOD
    var title_to_delete;
    main_data.vods.forEach(element => {
        if (element.id === id) {
            title_to_delete = element.title;
        }
    })

    if (window.confirm(`Do you want to delete ${title_to_delete}?`)) {
        fetch(`/vod/${id}`, { method: "delete" }).then(() => { window.location.reload() });
    }
}

fetch("/all_vods").then(res => res.json()).then(data => {
    main_data = data;
    data.vods.forEach(element => {
        var newVod = document.createElement("div");
        newVod.classList.add("border")
        newVod.classList.add("p-3")
        newVod.innerHTML = `<b>${element.title}</b>
        <button class="btn btn-primary ml-5" data-toggle="modal" data-target="#myModal" onclick=edit(${element.id})>Edit</button>
        <button class="btn btn-danger ml-3" onclick=deleteVod(${element.id})>Delete VOD</button>`;
        document.getElementById("vods").appendChild(newVod)
    });

});