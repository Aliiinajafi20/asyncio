import random
from time import sleep
import asyncio

def task(num):
    "Synchronous tasks"
    sleep(random.randint(0,2)*0.001)
    print('Task %s done'% num)

async def task_coro(num):
    "Coroutine tasks"
    await asyncio.sleep(random.randint(0,2)*0.001)
    print('Task %s done'% num)


def synchronous():
    for i in range(1,10):
       task(i)


async def asynchronous():
    tasks = [task_coro(i) for i in range(1,10)]
    await asyncio.gather(*tasks)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asyncio.run(asynchronous())