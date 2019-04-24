import time
import dask
import dask.dataframe as dd

# Make dataframe
df = dask.datasets.timeseries()
print('DataFrame Heads')
print(df.head())

# Use Standard Pandas Operations
df2 = df[df.y > 0]
df3 = df2.groupby('name').x.std()
print(df3)

t = time.time()
result = df3.compute()
#print(result)
print('Time dask.dataframe: '+str(time.time()-t))

from dask.distributed import Client, progress
client = Client('localhost:8786')
print(client)

t = time.time()
result = df3.compute()
#print(result)
print('Time dask.dataframe distributed: '+str(time.time()-t))

