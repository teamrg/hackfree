import pyglet
import songsprocess as sp
from learn import clf
import sys

#select a song with a thing?, let's say file is in variable song?
song = sys.argv[1]
samples = sp.transform(sp.wav_to_amps(song))
clusters = clf.predict(samples) #array of 0s 1s and 2s, a segment every 40ms
#play song


