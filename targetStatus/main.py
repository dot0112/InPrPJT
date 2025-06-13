import psutil
import time
from datetime import datetime

with open("./cpu.log", "w+", encoding="utf-8") as cpuF:
    with open("./mem.log", "w+", encoding="utf-8") as memF:
        psutil.cpu_percent(interval=None)
        while True:
            timeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            cpu_usage = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory()
            cpuF.write(f"({timeNow}) {psutil.cpu_percent()}\n")
            memF.write(f"({timeNow}) {mem.percent}\n")
            cpuF.flush()
            memF.flush()
            time.sleep(0.5)
