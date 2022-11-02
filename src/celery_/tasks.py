import logging
import time

from celery import Celery

celery_ = Celery(
    __name__,
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

logger = logging.getLogger(__name__)
sh = logging.StreamHandler()
logger.setLevel(logging.INFO)
logger.addHandler(sh)

@celery_.task(name='hello.task', bind=True)
def hello_task(self, name_='unset'):
    time.sleep(1)
    logger.info(f"hello_task {self}")
    return {"result": f"hello {name_}"}