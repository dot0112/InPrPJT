from app.utils import PngUtils
from app.models import singleton
import time
import psutil
import socket


@singleton
class StatusUtils:
    def __init__(self):
        self.startTime = 0
        self.pngUtils = PngUtils()
        from app.tasks import ManageBot

        self.manageBot = ManageBot()

    def setStartTime(self):
        self.startTime = time.time()

    def getUptime(self):
        uptime = round(time.time() - self.startTime, 2)
        return uptime

    def getCpuUsage(self):
        cpu_usage = psutil.cpu_percent(interval=0.5)
        return cpu_usage

    def getMemoryUsage(self):
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        return memory_usage

    def getAvailableMemory(self):
        memory = psutil.virtual_memory()
        availableMemory = memory.available
        return availableMemory

    def getIpAddress(self):
        hostname = socket.gethostname()
        ipAddress = socket.gethostbyname(hostname)
        return ipAddress

    def getStatus(self):
        return {
            "status": "ok",
            "uptime": f"{self.getUptime()} s",
            "cpuUsage": f"{self.getCpuUsage()} %",
            "memoryUsage": f"{self.getMemoryUsage()} %",
            "availableMemory": f"{self.getAvailableMemory() // (1024 * 1024)} MB",
            "ipAddress": self.getIpAddress(),
            "packetSaved": self.pngUtils.checkPNGData(),
            "latest bot count": self.manageBot.getLatestCount(),
        }
