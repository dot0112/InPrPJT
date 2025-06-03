from app.tasks import CliManage
from app.models import singleton
from app.utils.getch import getch
import time


@singleton
class Cli:
    def __init__(self):
        self.commands = {}
        self.cliManage = CliManage()

        self.command("s", "status")(self.handleStatus)
        self.command("n", "now")(self.handleTime)
        self.command("c", "check")(self.handleCheck)
        self.command("p", "packet")(self.handlePacket)

    def command(self, *names):
        def decorator(func):
            for name in names:
                self.commands[name] = func
            return func

        return decorator

    def run(self):
        while True:
            cmd = input("[Terminal] Enter Command: ").strip()
            func = self.commands.get(cmd)
            if func:
                func()
            else:
                print(f"Invalid Command: {repr(cmd)}")

            getch("Press Any Key...\n")
            time.sleep(0.1)

    def handleStatus(self):
        self.cliManage.printStatus()

    def handleTime(self):
        self.cliManage.printTime()

    def handleCheck(self):
        self.cliManage.printCheck()

    def handlePacket(self):
        self.cliManage.printPacket()
