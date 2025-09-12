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

async def example4() :
    print("[example4]")
    
    task1 = asyncio.create_task(coroutine1)
    task2 = asyncio.create_task(coroutine2)

    print("tasks created in event loop")