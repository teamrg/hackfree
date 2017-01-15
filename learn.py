from sklearn import cluster
import numpy as np
data = np.loadtxt('test.txt', ndmin=2)
clf = cluster.MiniBatchKMeans(n_clusters=3).fit(data)

