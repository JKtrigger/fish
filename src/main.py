from socket import gethostname

from fastapi import FastAPI, Request

from src import settings
from src.celery.tasks import celery_

app = FastAPI()


@app.get("/")
async def root(request: Request):
    task_name = "hello.task"
    text = tuple(request.query_params.keys())
    task = celery_.send_task(task_name, args=text)
    return {
        "message": "Hello world",
        "gethostname": gethostname(),
        "env": settings.config,
        "task.id":task.id,
        "url": f"http://localhost:5566/task/{task.id}"
    }
