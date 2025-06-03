import time
from app.tasks.scheduler import MainScheduler


def create_app():
    mainScheduler = MainScheduler()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            pass
