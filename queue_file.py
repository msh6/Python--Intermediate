from threading import  Thread, Lock
import time
from queue import Queue

    
if __name__ == "__main__":
    
    q = Queue()
    
    q.put(1)
    q.put(2)
    q.put(3)
    
    # 3 2 1 -->
    first = q.get()
    
    q.task_done()
    q.join()
    
    
    print("end of main")