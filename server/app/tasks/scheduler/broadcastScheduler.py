from app.models import singleton
from app.tasks import ManageBot
from app.utils import PngUtils
from apscheduler.schedulers.background import BackgroundScheduler


@singleton
class BoradcastScheduler:
    def __init__(self, test=False):
        self.manageBot = ManageBot()
        self.pngUtils = PngUtils()
        self.scheduler = BackgroundScheduler()
        if not test:
            self.scheduler.add_job(
                func=self.broadcastPacket, trigger="cron", minute="*/10", second=0
            )
            self.scheduler.add_job(
                func=self.stopBrodcastPacket, trigger="cron", minute="*/10", second=30
            )
        else:
            self.scheduler.add_job(func=self.broadcastPacket, trigger="cron", second=0)
            self.scheduler.add_job(
                func=self.stopBrodcastPacket, trigger="cron", second=30
            )
        self.scheduler.start()

    def broadcastPacket(self):
        self.manageBot.setBroadCast(True)
        self.manageBot.setBoradCastData(PngUtils().readPNGData().getBroadcastData())
        print("broadcastPacket()")

    def stopBrodcastPacket(self):
        self.manageBot.newBotCount()
        self.manageBot.setBroadCast(False)
        self.manageBot.setBoradCastData("")
        self.pngUtils.cleanPNGData()
        print("stopBroadcastPacket()")
