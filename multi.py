from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)
           
processes = []
num_processess = os.cpu_count()

#create processes
for i in range(num_processess):
    p = Process(target=square_numbers)
    processes.append(p)
    
for p in processes:
    print(p)
    
# start
for p in processes:
    p.start()
    
# join
for p in processes:
    p.join()

print("End of main")