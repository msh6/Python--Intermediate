from threading import  Thread, Lock, current_thread
import time
from queue import Queue

def worker(q, lock):
    while True:
         value = q.get()
         #processing
         with lock:
            print(f'in {current_thread().name} got {value}')
         q.task_done()
    
if __name__ == "__main__":
    
    lock = Lock()
    q = Queue()
    num_threads = 10
    
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()
        
    for i in range(1,21):
        q.put(i)
        
    q.join()
    
    print("end of main")