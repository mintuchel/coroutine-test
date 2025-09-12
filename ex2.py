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
    
    # nonblocking으로 event loop에 해당 코루틴에 대한 task만 생성해서 등록하고 바로 return
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    
    print("tasks created in event loop")

    await task1
    await task2

asyncio.run(example2())

# [example2]
# tasks created in event loop
# [1] start
# [2] start
# [1] finish
# [2] finish