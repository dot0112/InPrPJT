from app.models import singleton
from app.utils import PngUtils


@singleton
class ManageBot:
    def __init__(self):
        self.broadcast = False
        self.broadcastData = None
        self._botCount = {"now": 0, "latest": 0}

    def increaseBotCount(self):
        self._botCount["now"] += 1
        return self._botCount["now"]

    def newBotCount(self):
        self._botCount = {"now": 0, "latest": self._botCount["now"]}

    def getLatestCount(self):
        return self._botCount["latest"]

    def setBroadCast(self, flag):
        self.broadcast = flag

    def setBoradCastData(self, data):
        self.broadcastData = data
