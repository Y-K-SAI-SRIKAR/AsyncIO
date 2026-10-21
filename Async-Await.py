import asyncio

async def squared(num):
    return num*num

async def main():
    x = await squared(5)
    print(f"X:{x}")

    y = await squared(7)
    print(f"Y:{y}")

    z = x+y
    print(f"Sum:{z}")

asyncio.run(main())

#Explanation:
"""
Here, the routines squared() and main() are co-routines and asynchronous tasks.
the main will be paused until the x , y values from the squared routine are returned from the flow of execution.

The main use of await keyword is, it will pause the main() at point where x is called from calling y spontaneously.
It will make the main() to wait until a response for x is received from squared() routine.

Both these will be executed in the event loop automatically created from asyncio.run().

"""