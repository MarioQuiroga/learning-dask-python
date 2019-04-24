import dask.dataframe as dd
import dask.datasets as ds
import time
from dask_ml.linear_model import LogisticRegression
from dask_glm.datasets import make_classification

X, y = make_classification(n_samples=1000)

t = time.time()
lr = LogisticRegression()
lr.fit(X, y)
lr.predict(X)
lr.predict_proba(X)
#est.score(X, y)    
print('\nTime dask_ml: '+str(time.time()-t))

# Parallelize Scikit-Learn Directly
from dask.distributed import Client
from sklearn.externals.joblib import parallel_backend

client = Client('localhost:8786')  # Connect to a Dask Cluster
print(client)
with parallel_backend('dask', scatter=[X, y]):
    # Your normal scikit-learn code here    
    t = time.time()
    lr = LogisticRegression()
    lr.fit(X, y)
    lr.predict(X)
    lr.predict_proba(X)
    #est.score(X, y)    
    print('\nTime dask_ml distributed: '+str(time.time()-t))

