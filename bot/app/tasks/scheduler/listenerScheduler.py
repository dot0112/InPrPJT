from app.models import singleton
from app.tasks.listenBroadcast import ListenBroadcast
from .baseScheduler import BaseScheduler


@singleton
class ListenerScheduler:
    def __init__(self, test=False):
        self.baseScheduler = BaseScheduler()
        self.scheduler = self.baseScheduler.scheduler
        self.listenBroadcast = ListenBroadcast()
        if not test:
            print("add job */10 10")
            self.scheduler.add_job(
                func=self.listen, trigger="cron", minute="*/10", second=10
            )
        else:
            print("add job 10")
            self.scheduler.add_job(func=self.listen, trigger="cron", second=10)

    def listen(self):
        print("listen()")
        self.listenBroadcast.listen()
