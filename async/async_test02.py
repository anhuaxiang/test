import asyncio
import time
import async_timeout

loop = asyncio.get_event_loop()


async def fun_1(name):
    print(name)
    asyncio.sleep(5)
    print('time {}'.format(name))


async def fun_2():
    with async_timeout.timeout(2):
        await fun_1(22)


async def fun_3():
    for x in range(5):
        asyncio.ensure_future(fun_1('ensure'))
# loop.run_until_complete(fun_2())
t = [fun_1(i) for i in range(5)]
task_1 = asyncio.wait(t, timeout=1)
task_2 = fun_1('wait for')
task = asyncio.wait_for(task_2, 1)

# task_3 = asyncio.ensure_future(t)

loop.run_until_complete(fun_3())