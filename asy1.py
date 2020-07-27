import asyncio


async def foo():
    print('Runnimg in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('implicit context switch back to bar')



async def main():
    tasks = [foo(), bar()]
    await asyncio.gather(*tasks)


asyncio.run(main())