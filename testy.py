import classy
import songsprocess as sp

a, b = sp.wav_to_amps('Asleep.wav')
samples = sp.transform(a,b)
print(classy.clf.predict(samples))
