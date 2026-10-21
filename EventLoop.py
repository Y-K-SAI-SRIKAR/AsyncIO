import asyncio

loop = asyncio.new_event_loop()
async def task():
    print("Clocked for 5Sec IDLE Time")
    asyncio.sleep(5)
    print("Completed IDLE time")

loop.run_until_complete(task())
print("Completed Execution")
