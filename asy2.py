import time
import asyncio


start = time.time()

def tic():
    return 'at %1.1f seconds' %(time.time() - start)

async def gr1():
    print('gr1 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr1 ended work: {}'.format(tic()))

async def gr2():
    print('gr2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr2 ended work: {}'.format(tic()))

async def gr3():
    print('bia ye kar dige anjam bede ta vaghti ke coroutine ha black hastan,{}'.format(tic()))
    await asyncio.sleep(1)
    print('gr3 ended work: {}'.format(tic()))

async def main():
    tasks = [gr1(),gr2(),gr3()]
    await asyncio.gather(*tasks)

asyncio.run(main())

