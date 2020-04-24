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


class NoSoundTime:
    def __init__(self, amount_secs):
        self.amount_secs = amount_secs

    def play(self):
        time.sleep(self.amount_secs)


class Exercise:
    def __init__(self, base_path):
        self.elements = []
        self.base_path = base_path
        os.mkdir(base_path)

    def _add_sound(self, text):
        audio_path = self.base_path + text + ".mp3"
        save_audio(audio_path, text)
        self.elements.append(Sound(audio_path))

    def _add_time(self, length_secs, half_time_reminder=True):
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

    def _add_no_sound_time(self, length_secs):
        self.elements.append(NoSoundTime(length_secs))

    def add_exercise(self, exercise, time, rest_time):
        self._add_sound(exercise)
        self._add_time(time)
        self._add_sound("Done!")
        if rest_time != 0:
            self._add_sound("Rest!")
            self._add_time(rest_time)

    def add_rep_exercise(self, exercise, rep, time_per_rep, rest_time):
        self._add_sound(exercise)
        for i in range(rep):
            self._add_sound(str(i))
            self._add_no_sound_time(time_per_rep)
        self._add_sound("Done!")
        if rest_time != 0:
            self._add_sound("Rest!")
            self._add_time(rest_time)

    def play_exercise(self):
        for element in self.elements:
            element.play()