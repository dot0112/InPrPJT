from datetime import datetime
import requests
import time


def monitor(addr):
    with open("./log.txt", "w", encoding="utf-8") as logFile:
        while True:
            try:
                startTime = time.time()
                response = requests.get(f"http://{addr}", timeout=5)
                endTime = time.time()
                elapsedTime = (endTime - startTime) * 1000

                timeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

                logFile.write(
                    f"({timeNow}) status: {response.status_code} - {elapsedTime:.2f}ms\n"
                )
                logFile.flush()
            except requests.exceptions.RequestException as e:
                timeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                logFile.write(f"({timeNow}) 요청 실패: {e}\n")
                logFile.flush()

            time.sleep(0.5)
