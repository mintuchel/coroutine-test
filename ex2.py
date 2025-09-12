import asyncio

async def coroutine1() :
    print("[1] start")
    await asyncio.sleep(1)
    print("[1] finish")

async def coroutine2() :
    print("[2] start")
    await asyncio.sleep(1)
    print("[2] finish")

async def example2() :
    print("[example2]")
    
    task1 = asyncio.create_task(coroutine1)
    task2 = asyncio.create_task(coroutine2)
    
    print("tasks created in event loop")

    await task1
    await task2