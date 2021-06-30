import asyncio
import itertools
import sys


# fluent python 의 asyncio 부분 예제코드를 async / await 으로 수정.


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        write(status)
        flush()
        write("\x08" * len(status))
        try:
            await asyncio.sleep(0.2)
        except asyncio.CancelledError:
            break
    write(" " * len(status) + "\x08" * len(status))


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner_task = asyncio.create_task(spin(" thinking"))

    print("spinner object:", spinner_task)
    result = await slow_function()
    spinner_task.cancel()
    print(result)
    return result


def main():
    asyncio.run(supervisor())


if __name__ == "__main__":
    main()
