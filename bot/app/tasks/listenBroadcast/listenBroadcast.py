from app.models import PacketData
from app.tasks.encrypt import Encrypt
import requests
from datetime import datetime


class ListenBroadcast:
    def __init__(self):
        self.proxies = {
            "http": "socks5h://127.0.0.1:9050",
            "https": "socks5h://127.0.0.1:9050",
        }
        self.url = (
            "http://rahukukfy7szyt6r44meaxcwcw72x3nl4d2xxyogqbuwxx2nqoqnzjqd.onion"
        )
        self.packetData = PacketData()
        self.encrypt = Encrypt()
        self.rawData = b""
        self.callback = None

    def registerCallback(self, cb):
        self.callback = cb

    def listen(self):
        print("listen()")
        if self.get():
            self.parsePacket()

    def get(self):
        print("get()")
        try:
            is_onion = ".onion" in self.url
            proxies = self.proxies if is_onion else None

            response = requests.get(self.url, proxies=proxies, timeout=30)
            print(f"status: {response.status_code}")
            if response.status_code == 200:
                self.rawData = response.content
                return True
            else:
                return False
        except Exception as e:
            print(f"[ERROR] {type(e).__name__}: {e}")

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

        if self.callback:
            self.callback()

        self.packetData.updateTime = datetime.now()

    def decryptPacket(self, decryptData):
        self.packetData.ipAddr = list(decryptData[1:5])
        self.packetData.portNum = int.from_bytes(decryptData[5:7], "big")
        self.packetData.atkDate = [
            decryptData[7],
            decryptData[8],
            decryptData[9],
            decryptData[10],
            decryptData[11],
        ]
        self.packetData.atkDuration = decryptData[12]
