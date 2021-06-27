# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
async def f():
    await asyncio.sleep(0)
    return 123


async def main():
    result = await f()
    return result


# %%
