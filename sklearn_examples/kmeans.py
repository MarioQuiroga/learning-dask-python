from dask.distributed import Client
import time
#client = Client(processes=False, threads_per_worker=4, n_workers=1, memory_limit='2GB')
client = Client('localhost:8786')
print(client)

import dask
from distributed.utils import format_bytes

import dask_ml.cluster
import dask_ml.datasets


X, y = dask_ml.datasets.make_blobs(
    n_samples=100000,
    n_features=50,
    centers=3,
    chunks=10000,
)

format_bytes(X.nbytes)

X = X.persist()

km = dask_ml.cluster.KMeans(n_clusters=3, init_max_iter=2, oversampling_factor=10, random_state=0)

t = time.time()
km.fit(X)
print('Time kmeans distributed:' time.time()-t)
