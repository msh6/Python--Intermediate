from threading import  Thread, Lock
import time
from queue import Queue
database_value = 0

def increase(lock):
    global database_value
    
    with lock:
        #lock.acquire()
        local_copy = database_value
        #processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
        #lock.release()
    
if __name__ == "__main__":
    
    lock = Lock()
    print("Start value", database_value)
    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end value", database_value)
    print("End of main")