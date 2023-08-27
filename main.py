import sounddevice as sd
import numpy as np

from queue import Queue


audio_queue = Queue()


def read_sound(indata, frames, time, status):
    audio_queue.put(indata.copy())


with sd.InputStream(callback=read_sound):
    while True:
        volume_norm = np.linalg.norm(audio_queue.get()) * 10

        if volume_norm > 10:
            print(f"Your volume is: {volume_norm}")
