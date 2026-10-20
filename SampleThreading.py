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