# importing libraries

import sounddevice as sd
from scipy.io.wavfile import write
import wave as wv

#sampling frequency

freq = 44100
#duration
duration = 10
print("recording...")

#start recorder 
recording = sd.rec(int(duration * freq),samplerate = freq, channels=2)

# record audio 
sd.wait()

#convert  NumPy array to an audio file

write("recording0.wav",freq,recording)
wv.write("recording1.wav",freq,recording)
print("recording is completed")
