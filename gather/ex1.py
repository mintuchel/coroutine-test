import asyncio
import time

async def coroutine1() :
    print("[1] start")
    await asyncio.sleep(3)
    print("[1] finish")

async def coroutine2() :
    print("[2] start")
    await asyncio.sleep(5)
    print("[2] finish")

async def example1() :
    print("[example1]")
    start = time.time()
    # 인자로 받은 코루틴들을 동시에 실행시키고 모든 코루틴이 끝날때까지 기다림
    await asyncio.gather(coroutine1(), coroutine2())
    print(time.time()-start)

asyncio.run(example1())

# [example1]
# [1] start
# [2] start
# [1] finish
# [2] finish
# 5.001953125