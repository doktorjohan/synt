#initial commit stuff
import pyaudio
import numpy as np

FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100 # muuda vastavalt süsteemile

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)

freq = 440
duration = 2000.0

sound = (np.sin(2*np.pi*np.arange(freq*duration)*freq/RATE)).astype(np.float32)

stream.write(sound)

stream.stop_stream()
stream.close()

p.terminate()