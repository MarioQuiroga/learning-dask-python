import numpy as np
import time

print('Time Sequential')
t = time.time()
x = np.random.rand(10000,10000)
y = x + x.T
z = y[::2, 5000:].mean(axis=1)
print(z)
print('Time with NumPy: '+str(time.time()-t))

from dask.distributed import Client, progress
client = Client('localhost:8786')
print('\nTime Distributed')
print(client)

# Make random data
import dask.array as da
t = time.time()
x = da.random.random((10000, 10000), chunks=(1000, 1000))
y = x + x.T
z = y[::2, 5000:].mean(axis=1)

result = z.compute()
print(result)
print('Time with Dask Array: '+str(time.time()-t))
