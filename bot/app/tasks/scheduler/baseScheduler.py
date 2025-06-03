from app.models import singleton
from apscheduler.schedulers.background import BackgroundScheduler


@singleton
class BaseScheduler:
    def __init__(self):
        self._scheduler = BackgroundScheduler()
        self.start()

    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()

    def shutdown(self):
        if self.scheduler.running:
            self.scheduler.shutdown()

    @property
    def scheduler(self):
        return self._scheduler

    @scheduler.setter
    def scheduler(self, value):
        self._scheduler = value
