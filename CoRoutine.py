import asyncio

async def greet():
    print("Clocked for 2s Idle State")
    asyncio.sleep(2)
    print("Have a Nice Day")
asyncio.run(greet())

#Notes:
"""
Synchronous Tasks: The tasks or process which will execute in sequential order following Queue principle.
Asyncronous: The tasks wihich undergo execution of a task while another task is already in executing state.

Multi-Processing : Parallel execution of multiple tasks at a time.
Multi-Threading : It is about workers or execution units in a single process.

Co-Routines: 
Routines are nothing but the functions or tasks which are co-operative with other tasks.
CoRoutines will pause their execution for other routines to execute by utilizing fewer threads,
and will continue execution from the point of pause of the same routine.

for Asynchronous tasks to execute , there is a requirement of Event Loop.
Event loop is a runtiume mechanism which ensures the execution status of the routines.

"""