from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import pandas as pd
import time

# Make data
X, y = make_classification(n_samples=1000, random_state=0)
print(X[:5])

param_grid = {"C": [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0],
              "kernel": ['rbf', 'poly', 'sigmoid'],
              "shrinking": [True, False]}

grid_search = GridSearchCV(SVC(gamma='auto', random_state=0, probability=True),
                           param_grid=param_grid,
                           return_train_score=False,
                           iid=True,
                           cv=3,
                           n_jobs=-1)

# To fit that normally, we would call
t = time.time()
grid_search.fit(X, y)
print('Time fit normally: '+str(time.time()-t))

# To fit it using the cluster, we just need to use a context manager provided by joblib.
from dask.distributed import Client, progress
from sklearn.externals import joblib
client = Client(processes=False, threads_per_worker=4, n_workers=1, memory_limit='2GB')
#client = Client('localhost:8786)
print(client)

t = time.time()
with joblib.parallel_backend('dask'):
    grid_search.fit(X, y)
print('Time fit distributed: '+str(time.time()-t))

print(pd.DataFrame(grid_search.cv_results_).head())

print(grid_search.predict(X)[:5])

print(grid_search.score(X, y))

