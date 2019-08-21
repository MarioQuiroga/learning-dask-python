import time
from dask import compute, delayed
from dask.distributed import Client
N = 5

def inc(x):
    time.sleep(1)
    return x + 1

inputs = [0 for i in range(N)] # Make data

t = time.time()
results = [inc(x) for x in inputs]  # Sequential compute
print('Time sequential: '+str(time.time()-t))
print(results)

t = time.time()
values = [delayed(inc)(x) for x in inputs] # Make tasks
print('Time build dask computation: '+str(time.time()-t))

client = Client("localhost:8786")
print(client)
t = time.time()
results = compute(*values, scheduler='distributed') # Distributed compute
print('Time distributed: '+str(time.time()-t))
print(results)
