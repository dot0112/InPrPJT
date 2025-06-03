from app.utils import PngUtils
from app.models import singleton


@singleton
class CheckCli:
    def __init__(self):
        self.packetData = None
        self.pngUtils = PngUtils()

    def cliPrint(self):
        if not self.pngUtils.checkPNGData():
            print("Data Empty")
        else:
            self.packetData = self.pngUtils.readPNGData()
            self.packetData.printPacket()
