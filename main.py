from tkinter import messagebox
import sounddevice as sd
import numpy as np

from queue import Queue

VOLUME_THRESHOLD = 15
audio_queue = Queue()
was_too_loud = False


def read_sound(indata, frames, time, status):
    audio_queue.put(indata.copy())


with sd.InputStream(callback=read_sound):
    while True:
        volume_norm = np.linalg.norm(audio_queue.get()) * 10

        if volume_norm > VOLUME_THRESHOLD and not was_too_loud:
            was_too_loud = True
            messagebox.showwarning("You're too loud!",
                                   f"Volume: {volume_norm}")
        elif volume_norm < VOLUME_THRESHOLD and was_too_loud:
            was_too_loud = False
