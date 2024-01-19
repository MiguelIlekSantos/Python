import threading
import time

#thread  = a flow of execution, like a seperate order of intruction.
#                 However each thread takes a turn running to achive concurrency
#                 GIL = (Global interpreter lock)
#                 allows only one thread to hold the control of the phyton interpreter

# cpu bound = program/ task spends most of its time waiting for internal events (CPU intensive)
#                       use multiprocessing

#io bound = program/ task spends most of it's time waiting for external events (user input, wab scraping)
#                   use multithreading


def eat_breakfast():
    time.sleep(3)
    print("You are eating a breakfast")

def drink_coffee():
    time.sleep(4)
    print("You are drinking coffee")

def study():
    time.sleep(5)
    print("You are studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()
#eat_breakfast()
#drink_coffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())