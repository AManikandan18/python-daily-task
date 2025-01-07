import time
import asyncio

##def sync():
##    print("start sync")
##    time.sleep(2)
##    print("end sync")


async def asyncno():
    print("start async")
    await asyncno()
    print("end async")

asyncio.run(asyncno())

##sync()

