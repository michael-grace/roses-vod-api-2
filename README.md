# Roses VOD API

### Running
* `python3 -m venv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`
* `python3 app.py`

### API

* `GET /all_vods`

Response: 
```
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

* `POST /vod`

To Describe

* `PUT /vod/id`

To Describe

* `DELETE /vod/id`

To Describe

### TODO (on Thursday)
* Interface