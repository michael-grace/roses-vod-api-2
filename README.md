# Roses VOD API

### Running
* `python3 -m venv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`
* `python3 app.py`

### API

---

* `GET /all_vods`

Response: 
```json
{
    "vods": [
        {
            "id": 123,
            "title": "VOD Title",
            "description": "VOD Description",
            "url": "vod-url"
        }
    ]
}
```

---

* `POST /vod`

Request Body:
```json
{
    "title": "New VOD Title",
    "description": "New VOD Description",
    "url": "New VOD URL"
}
```

OK Response:
```json
{
    "id": 123,
    "title": "New VOD Title",
    "description": "New VOD Description",
    "url": "New VOD URL"
}
```

---

* `PUT /vod/{id}`

Parameters:
* `id`: The ID number of the VOD to be edited

Request Body:
```json
{
    "title": "New VOD Title",
    "description": "New VOD Description",
    "url": "New VOD URL"
}
```

*Note:* All fields must be provided, even if the data doesn't change. A `400 Bad Request` response will be returned otherwise

OK Response:
```json
{
    "id": 123,
    "title": "New VOD Title",
    "description": "New VOD Description",
    "url": "New VOD URL"
}
```

---

* `DELETE /vod/{id}`

Parameters:
* `id`: The ID number of the VOD to be edited

OK Response:
```json
{
    "Deleted": 123
}
```

---

### Interface

Available at `/manage`