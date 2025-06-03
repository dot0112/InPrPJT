from app.models import PacketData
from app.tasks.encrypt import Encrypt
import requests
from datetime import datetime


class ListenBroadcast:
    def __init__(self):
        self.url = ""
        self.packetData = PacketData()
        self.encrypt = Encrypt()
        self.rawData = b""
        self.callback = None

    def registerCallback(self, cb):
        self.callback = cb

    def listen(self):
        if self.get():
            self.parsePacket()

    def get(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.rawData = response.content
            if self.callback:
                self.callback()
            return True
        else:
            return False

    def parsePacket(self):
        if not self.rawData or len(self.rawData) < 1:
            return

        self.packetData.flag = self.rawData[0]

        if self.packetData.flag == 3:
            self.packetData.clear()
        elif self.packetData.flag == 1:
            self.packetData.encryptedToken = self.rawData[1:]
            decryptData = self.encrypt.decrypt(self.packetData.encryptedToken)
            if decryptData is not None:
                self.decryptPacket(decryptData)
        elif self.packetData.flag == 2:
            self.encrypt.key = self.rawData[1:]
            decryptData = self.encrypt.decrypt(self.packetData.encryptedToken)
            if decryptData is not None:
                self.decryptPacket(decryptData)

        self.packetData.updateTime = datetime.now()

    def decryptPacket(self, decryptData):
        self.packetData.ipAddr = list(decryptData[0:4])
        self.packetData.portNum = int.from_bytes(decryptData[4:6], "big")
        self.packetData.atkDate = [
            decryptData[6],
            int.from_bytes(decryptData[7:9], "big"),
            decryptData[9],
        ]
        self.packetData.atkDuration = decryptData[10]
