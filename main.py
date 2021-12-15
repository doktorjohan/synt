import numpy as np
import pyaudio
'''
RATE ja FRAMES_PER_BUFFER muutujad ebakindlad, vastavalt süsteemile võivad olla erinevad


'''
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 1024

core_options = {
    'rate': RATE,
    'channels': CHANNELS,
    'format': FORMAT,
    'output': True,
    'input_device_index': None,
    'output_device_index': 3,
    'frames_per_buffer': FRAMES_PER_BUFFER,
    'start': True
}


core = pyaudio.PyAudio()
stream = core.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   output=True)

# sisaldab heli 'valemit'
def sound_generator(freq, octave=1):
    sound = (np.sin(2*np.pi*freq*octave/RATE*np.arange(RATE, dtype=np.float32)))
    stream.write(sound)
