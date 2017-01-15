from sklearn import cluster
import numpy as np
from time import time
t0=time()
data = np.loadtxt('test.txt', ndmin=2)
t1=time()
clf = cluster.MiniBatchKMeans(n_clusters=3).fit(data)
t2=time()
print(t1-t0)
print(t2-t1)

