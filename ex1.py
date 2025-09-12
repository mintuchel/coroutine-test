import asyncio

async def coroutine1() :
    print("[1] start")
    # 해당 코루틴의 제어권을 1초동안 반환
    # asyncio 이벤트 루프 내 다른 코루틴들이 실행될 수 있게
    await asyncio.sleep(1)
    print("[1] finish")

async def coroutine2() :
    print("[2] start")
    await asyncio.sleep(1)
    print("[2] finish")

async def example1() :
    print("[example1]")
    await coroutine1()
    await coroutine2()

asyncio.run(example1())

# [example1]
# [1] start
# [1] finish
# [2] start
# [2] finish