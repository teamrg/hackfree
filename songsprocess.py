import wave, struct, sys, os
import numpy as np
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt

def wav_to_amps(filename):
    w = wave.open(filename)
    fr = w.getframerate()
    astr = w.readframes(w.getnframes())
    a = struct.unpack("%ih" % (w.getnframes()*w.getnchannels()), astr)
    a = [float(val) / pow(2, 15) for val in a]
    return a, fr;

final=[]
j = 0
for f in os.listdir():
    samples=[]
    if f.endswith('.wav'):
        j += 1
        print(j)
        proc, r = wav_to_amps(f)
        l = r*.04
        s = []
        for frame in proc:
            if len(s)<l:
              s+=[frame]
            else:
                samples+=[s]  
                s=[]
        i = 0;
        while i < len(samples):
            samples[i] = np.fft.fft(samples[i])
            samples[i]=pow(samples[i].real,2)+pow(samples[i].imag,2)
            final += [sum(samples[i])]
            i+=1

np.savetxt('test.txt',final)
    
