import time
from dask.distributed import Client
client = Client('localhost:8786')
print(client)

N = 5 # length array

def inc(x):
    time.sleep(1) # Time in seconds
    return x + 1

c = client.submit(inc, 0) # Send 1 task to cluster, return 1 future
c = c.result() # block until work finishes, then gather result
#print(c)
array = [0 for i in range(N)]

y_s = []
s = time.time()
for i in range(N):  # Sequential version to inc
    y_s.append(inc(array[i]))

f = time.time()
print('Time sequential: '+str(f-s)) 
print(y_s)

s = time.time()
x = client.map(inc, array) # Send list task, return future list
y = client.gather(x)
f = time.time()

print('Time distributed: '+str(f-s)) 
print(y)


