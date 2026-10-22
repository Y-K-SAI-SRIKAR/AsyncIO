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
    task1 = asyncio.create_task(production())
    task2 = asyncio.create_task(debug())
    await task1
    await task2 

asyncio.run(main())
end = time.time()
print("Time Taken to execute:",end-start)

#Notes
"""
The above program implements concurrent execution, as we have uised tasks for parallel execution.

The reason behind this behaviour is that asynchronous programming deals with coroutines, and 
using async and await along with task creation execute multiple routines execute concurrently.

When one task suspends its execution while waiting for an operation to complete, 
the event loop can execute other scheduled tasks.

"""