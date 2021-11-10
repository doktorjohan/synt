#initial commit stuff
import pyaudio
import numpy as np
from scipy import signal

FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100  # muuda vastavalt süsteemile
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


def sound_generator(freq):
    sound = (np.sin(2*np.pi*freq/RATE*np.arange(RATE, dtype=np.float32)))
    stream.write(sound)


'''
stream.stop_stream()
stream.close()
core.terminate()
'''


