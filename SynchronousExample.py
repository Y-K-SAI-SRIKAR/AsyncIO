import asyncio
import time

start = time.time()

async def production():
    await asyncio.sleep(7)
    print("Project into Production")

async def debug():
    await asyncio.sleep(3)
    print("Debugging done!")

async def main():
    await production()
    await debug()

asyncio.run(main())
end = time.time()
print("Time Taken to execute:",end-start)

#Notes
"""
The above program implements sequential execution, even though we have used async and await keywords.

The reason behind this behaviour is that asynchronous programming deals with coroutines, and 
simply using async and await does not automatically execute multiple routines concurrently.

When one task suspends its execution while waiting for an operation to complete, 
the event loop can execute other scheduled tasks.

"""