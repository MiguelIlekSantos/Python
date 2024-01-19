# deamon threads = a thread that runs in the background, not important for program to run
#                                  your program will not wait for deamon threads to complete before exiting
#                                  non-deamon threads cannot normally be killed stay alive until task is complete

#                                  ex. back ground task, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ",count, "seconds")

x= threading.Thread(target=timer,daemon=True)
x.start()

answer = input("Write something: ")
print(x.isDaemon())