import time
from app.tasks.scheduler import MainScheduler


def create_app(test=False):
    mainScheduler = MainScheduler(test)
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
            # pass
