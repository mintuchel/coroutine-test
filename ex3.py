import asyncio

async def coroutine1() :
    print("[1] start")
    # 현재 코루틴 객체 1초동안 sleep
    await asyncio.sleep(1)
    print("[1] finish")

async def coroutine2() :
    print("[2] start")
    # 현재 코루틴 객체 1초동안 sleep
    await asyncio.sleep(1)
    print("[2] finish")

async def example3() :
    print("[example3]")

    task1 = asyncio.create_task(coroutine1)
    task2 = asyncio.create_task(coroutine2)

    # 현재 example3 코루틴 객체 3초동안 sleep
    await asyncio.sleep(3)
    print("tasks created in event loop")
      
    await task1
    await task2