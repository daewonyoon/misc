import asyncio
import time


async def main():
    print(f"{time.ctime()}: Hello")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()}: Goodbye!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancle()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
