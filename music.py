import pyglet
import songsprocess as sp
from sklearn import cluster
from sklearn.externals import joblib
import sys
import os.path

#select a song with a thing?, let's say file is in variable song?
song = sys.argv[1]
print(song.replace('.wav','.pk1'))
if os.path.exists(song.replace('.wav','.pk1')):
    clf = joblib.load(song.replace('.wav', '.pk1'))
    print("This song exists yay")
else:
    print("New song wow")
    a, b = sp.wav_to_amps(song)
    samples = sp.transform(a,b)
    clf = cluster.KMeans(n_clusters=4).fit(samples)
    joblib.dump(clf, song.replace('.wav','.pk1'))
clusters =clf.labels_.tolist() #array of 0s 1s and 2s, a segment every 40ms
print(clusters)
#play song


