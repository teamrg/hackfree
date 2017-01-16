import wave, struct, os
import numpy as np
import scipy.io.wavfile as wf
def wav_to_amps(filename):
    w = wave.open(filename, 'r') #open wave file as read only
    fr = w.getframerate() #need this for segmentation later
    nframe = w.getnframes()
    nchan = w.getnchannels()
    astr = w.readframes(nframe) #get frames
    a = struct.unpack("%ih" % (nframe*nchan), astr) #bit stuff
    a = [float(val) / pow(2,15) for val in a] #normalization
    w.close() #close
    return a, fr*nchan; #return amplitudes array and the framerate

def transform(proc, r):
    l=r*.25 #segment length of .25s of frames
    s=[] #contains segment
    samples = [] #all segments in song
    for frame in proc: 
        if len(s) < l:
            s += [frame] #add 40ms of frames
        else:
            samples += [s]
            s = []
    i = 0
    while i < len(samples):
        """samples[i] = np.fft.fft(samples[i]) #fourier transform
        samples[i] = pow(samples[i].real, 2) + pow(samples[i].imag, 2) #magnitude of power spectrum"""
        samples[i] = [sum(samples[i])]
        i += 1
    return samples

def procdir(txtfl):
    final = []
    for f in os.listdir('./Songs'):
        if f.endswith('.wav'): #do stuff to every wav in directory
            proc, r = wav_to_amps(f)
            final += transform(proc,r)
    np.savetxt(txtfl, final)

