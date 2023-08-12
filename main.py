# generate localhost certfile using mkcert
# gunicorn main:app --certfile /path/to/certfile --keyfile /pat/to/keyfile --workers 4 --worker-class uvicorn.workers.UvicornWorker
# gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind unix:/tmp/gunicorn.sock

import fastapi

app = fastapi.FastAPI()


@app.get("/")
def hello():
    return "hello world"
