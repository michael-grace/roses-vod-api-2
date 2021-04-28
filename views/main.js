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
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            window.location.reload();
        };
        xhttp.open("PATCH", `/vod/${id}`, true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(JSON.stringify({
            "title": document.getElementById("vod-title").value,
            "description": document.getElementById("vod-description").value,
            "url": document.getElementById("vod-url").value,
        }));
    }

}

const addVod = () => {
    document.getElementById("vod-submit").onclick = () => {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            window.location.reload();
        };
        xhttp.open("POST", "/vod", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(JSON.stringify({
            "title": document.getElementById("vod-title").value,
            "description": document.getElementById("vod-description").value,
            "url": document.getElementById("vod-url").value,
        }));
    }
}

fetch("/all_vods").then(res => res.json()).then(data => {
    main_data = data;
    data.vods.forEach(element => {
        var newVod = document.createElement("div");
        newVod.classList.add("border")
        newVod.classList.add("p-3")
        newVod.innerHTML = `<b>${element.title}</b><button class="btn btn-primary ml-5" data-toggle="modal" data-target="#myModal" onclick=edit(${element.id})>Edit</button>`;
        document.getElementById("vods").appendChild(newVod)
    });

});