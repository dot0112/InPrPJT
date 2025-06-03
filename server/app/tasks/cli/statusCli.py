from app.models import singleton
from app.utils import StatusUtils


@singleton
class StatusCli:
    def __init__(self):
        self.statusUtil = StatusUtils()

    def cliPrint(self):
        status = self.statusUtil.getStatus()
        for category, condition in status.items():
            print(f"{category} : {condition}")
