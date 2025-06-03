from app.models import singleton
from .checkCli import CheckCli
from .statusCli import StatusCli
from .timeCli import TimeCli
from .packetCli import PacketCli


@singleton
class CliManage:
    def __init__(self):
        self.checkCli = CheckCli()
        self.statusCli = StatusCli()
        self.timeCli = TimeCli()
        self.packetCli = PacketCli()

    def printCheck(self):
        self.checkCli.cliPrint()

    def printStatus(self):
        self.statusCli.cliPrint()

    def printTime(self):
        self.timeCli.cliPrint()

    def printPacket(self):
        self.packetCli.cliPrint()
