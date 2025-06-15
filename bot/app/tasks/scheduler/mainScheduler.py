from .listenerScheduler import ListenerScheduler
from .attackScheduler import AttackScheduler


class MainScheduler:
    def __init__(self, test=False):
        self.listenerScheduler = ListenerScheduler(test)
        self.attackScheduler = AttackScheduler()
        self.listenerScheduler.listenBroadcast.registerCallback(
            self.attackScheduler.onDataReceived
        )
