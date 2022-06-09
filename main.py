import asyncio
import random
from asyncio import sleep


async def f():
    while True:
        print("f() func")
        await asyncio.sleep(1)


def g_helper():
    return random.randint(0, 100)


async def g():
    while True:
        print(g_helper())
        await asyncio.sleep(1)


async def main():
    main_loop.create_task(g())
    main_loop.create_task(f())
    await f()


main_loop = asyncio.get_event_loop()

main_loop.run_until_complete(main())
main_loop.run_forever()
