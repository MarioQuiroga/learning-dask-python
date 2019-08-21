import time
import dask

def inc(x):
    time.sleep(1)
    return x + 1

def dec(x):
    time.sleep(1)
    return x - 1
    
def add(x, y):
    time.sleep(1)
    return x + y

t = time.time()
x = inc(1)
y = dec(2)
z = add(x, y)
print('Time Execute sequential: '+str(time.time()-t))
print(z)

import dask
inc = dask.delayed(inc)
dec = dask.delayed(dec)
add = dask.delayed(add)
x = inc(1)
y = dec(2)
z = add(x, y)

t = time.time()
z.compute()
print('Time Execute with threads on our local machine: '+str(time.time()-t))

from dask.distributed import Client, progress
c = Client('localhost:8786')
print(c)

t = time.time()
z.compute()
print('Time Execute in Cluster: '+str(time.time()-t))

