from gtts import gTTS
from playsound import playsound
import time
import os


def save_audio(filename, text):
    if os.path.isfile(filename):
        return
    sound = gTTS(text=text, lang='en', slow=True)
    sound.save(filename)


class Sound:
    def __init__(self, audio_path):
        self.path = audio_path

    def play(self):
        playsound(self.path)


class Time:
    def __init__(self, amount_secs, audio_path, halftime_path=None):
        self.amount_secs = amount_secs
        self.path = audio_path
        self.halftime_path = halftime_path

    def play(self):
        if not self.halftime_path:
            playsound(self.path)
            time.sleep(self.amount_secs)
        else:
            playsound(self.path)
            time.sleep(self.amount_secs)


class Exercise:
    def __init__(self, base_path):
        self.elements = []
        self.base_path = base_path
        os.mkdir(base_path)

    def add_sound(self, text):
        audio_path = self.base_path + text + ".mp3"
        save_audio(audio_path, text)
        self.elements.append(Sound(audio_path))

    def add_time(self, length_secs, half_time_reminder=True):
        text = str(length_secs) + " seconds"
        audio_path = self.base_path + text + ".mp3"
        save_audio(audio_path, text)
        if half_time_reminder:
            half_time_text = "Half the time"
            half_time_path = self.base_path + half_time_text + ".mp3"
            save_audio(audio_path, text)
            self.elements.append(Time(length_secs, audio_path, half_time_path))
        else:
            self.elements.append(Time(length_secs, audio_path))

    def add_exercise(self, exercise, time, rest_time):
        self.add_sound(exercise)
        self.add_time(time)
        self.add_sound("Done!")
        if rest_time != 0:
            self.add_sound("Rest!")
            self.add_time(rest_time)

    def play_exercise(self):
        for element in self.elements:
            element.play()