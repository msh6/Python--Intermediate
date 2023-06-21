from multiprocessing import Process, Queue, Value, Array, Lock
import time

def square(numbers, queue, lock):
     for i in numbers:
        with lock:
            queue.put(i*i)
         
def make_negative(numbers, queue, lock):
    for i in numbers:
        with lock:
            queue.put(-1*i)


if __name__ == "__main__":
    
    lock = Lock()
    numbers = range(1, 5)
    q = Queue()
    
    p1 = Process(target = square, args= (numbers, q, lock))
    p2 = Process(target = make_negative, args= (numbers, q, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())
        
    