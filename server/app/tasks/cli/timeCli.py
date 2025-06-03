from app.models import singleton
from datetime import datetime
from zoneinfo import ZoneInfo


@singleton
class TimeCli:
    def __init__(self):
        self.zones = {
            "Asia": "Asia/Seoul",
            "Europe": "Europe/London",
            "North America": "America/New_York",
            "South America": "America/Sao_Paulo",
            "Oceania": "Australia/Sydney",
            "Africa": "Africa/Johannesburg",
            "Antarctica": "Antarctica/Palmer",
            "UTC": "UTC",
        }

    def getTime(self, timeZone):
        continent = list(self.zones.keys())[timeZone]
        now = datetime.now(ZoneInfo(self.zones[continent]))
        return f"{continent} ({self.zones[continent]}): {now.strftime('%Y-%m-%d %H:%M:%S')}"

    def cliPrint(self):
        for i, (continent, tzName) in enumerate(self.zones.items()):
            print(f"{i} : {continent}({tzName})")
        while True:
            try:
                timeZone = input("[Terminal] Choose Time Zone:")
                timeZone = int(timeZone.strip())
                if 0 <= timeZone < len(self.zones.items()):
                    print(self.getTime(timeZone))
                    break
                else:
                    print(f"Enter Number Between 0 ~ {len(self.zones.items()) - 1}")
            except ValueError:
                print("Enter Number Only")
