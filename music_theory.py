import numpy as np
import sounddevice as sd

class Note:
    def __init__(self, freq, duration=0.5, fs=44100):
        self.freq = freq
        self.duration = duration
        self.fs = fs
        
    def play(self):
        t = np.linspace(0, self.duration, int(self.fs*self.duration), endpoint=False)
        wav = np.sin(2 * np.pi * self.freq * t)
        sd.play(wav, samplerate=self.fs)
        sd.wait()
        

b = 261.63
f = 3/2
multiplier = [1, f, (f**2), (f**3), (f**4), 2]
sample = list(map(lambda x: b*x, multiplier))
for i in sample:
    print(i)
    Note(i).play()


b = 261.63
f = 3/2
multiplier = [1, f, (f**2), (f**3), (f**4), 2]
sample = list(map(lambda x: b*x, multiplier))

def half(n, max=b*2):
    if n > max:
        n = n/2
        if n > max:
            return half(n, max)
        return n
    return n

new_sample = list(map(half, sample))
print(new_sample)
for i in sorted(new_sample):
    print(i)
    Note(i).play()