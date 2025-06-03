from .listenerScheduler import ListenerScheduler
from .attackScheduler import AttackScheduler


class MainScheduler:
    def __init__(self):
        self.listenerScheduler = ListenerScheduler()
        self.attackScheduler = AttackScheduler()
