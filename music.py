import pyglet
import songsprocess as sp
from sklearn import cluster
import sys

#select a song with a thing?, let's say file is in variable song?
song = sys.argv[1]
a, b = sp.wav_to_amps(song)
samples = sp.transform(a,b)
clf = cluster.KMeans(n_clusters=4).fit(samples)
clusters =clf.labels_.tolist() #array of 0s 1s and 2s, a segment every 40ms
print(clusters)
#play song


