# Python program to illustrate the concept 
# of threading 
# importing the threading module 
from threading import Thread, Lock, local 
import time

shared_Data = 0

mutex = Lock()

def print_cube(num): 
    while True:
        global shared_Data
        mutex.acquire()
        print("T1 : " + str(shared_Data)) 
        shared_Data = shared_Data + 1
        mutex.release()
        time.sleep(3.0)

def print_square(num): 
    while True:
        global shared_Data
        mutex.acquire()
        print("T2 : " + str(shared_Data)) 
        # shared_Data = shared_Data + 1
        mutex.release()
        time.sleep(2.0)

if __name__ == "__main__": 
	# creating thread 
	t1 = Thread(target=print_square, args=(10,)) 
	t2 = Thread(target=print_cube, args=(10,)) 

	# starting thread 1 
	t1.start() 
	# starting thread 2 
	t2.start() 

	# wait until thread 1 is completely executed 
	t1.join() 
	# wait until thread 2 is completely executed 
	t2.join() 

	# both threads completely executed 
	print("Done!") 
