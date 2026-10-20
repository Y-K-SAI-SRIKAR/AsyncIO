import threading

def inf_loop():
    while True:
        pass

def greet():
    print("Hello, I am Srikar")


thread1 = threading.Thread(target=inf_loop)
thread2 = threading.Thread(target=greet)

thread1.start()
thread2.start()

#NOTES:
"""
Process is a program under Execution. Each and Every process requiures resources such as memory to complete their tasks.
No other processes can share the same resources. For a process to acquire or release resources the processes execution must be completed 
and withdrawn from the execution stack or queue for other process to allocate resources.

Part of a process or a smallest unit of execution is called as a Thread.
For a process there exist single or multiple threads. Here, the threads of a same process can share resources.

A multi-threaded process can perform multiple tasks or operations at a single unit of time.

**In the above program, inf_loop(), greet() were assigned different threads and they doesnot belong to same process.
so the threads 1 and 2 will be executed concurrently and as thread1 is infinite it never stops executing
and it doesnot prevent thread2 from executing.

Therefore, we get the result of thread2 first and thread1 is inifinte we could not get any output on the console.
"""