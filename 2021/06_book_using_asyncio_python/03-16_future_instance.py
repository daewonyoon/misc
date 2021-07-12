# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import asyncio


# %%
async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result("I have finished!")

loop = asyncio.get_event_loop()


# %%
fut = asyncio.Future()

print(fut.done())


# %%
loop.create_task(main(fut))


# %%
loop.run_until_complete(fut)


# %%
print(fut.done())


# %%
print(fut.result())


# %%



