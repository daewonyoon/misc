import asyncio


async def doubler(n):
    for i in range(n):
        yield i, i * 2
        await asyncio.sleep(0.1)


async def main():
    result = [x async for x in doubler(3)]
    print(result)
    result = {x: y async for x, y in doubler(3)}
    print(result)
    result = {x async for x in doubler(3)}
    print(result)


asyncio.run(main())
