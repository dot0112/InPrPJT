from app.models import singleton
from app.tasks.listenBroadcast import ListenBroadcast
from .baseScheduler import BaseScheduler


@singleton
class ListenerScheduler:
    def __init__(self):
        self.baseScheduler = BaseScheduler()
        self.scheduler = self.baseScheduler.scheduler
        self.listenBroadcast = ListenBroadcast()
        # self.scheduler.add_job(func=self.listen, trigger="cron", minute=0, second=10)
        self.scheduler.add_job(func=self.listen, trigger="cron", minute="*/2", second=10)

    def listen(self):
        self.listenBroadcast.listen()
