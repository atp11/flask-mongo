Basic blog application tutorial called [Flaskr](https://flask.palletsprojects.com/en/2.2.x/tutorial/) modified to use Mongo as a database.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
docker run -it --rm -p 27017:27017 mongo
```

```bash
flask --app flaskr --debug run
```

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

