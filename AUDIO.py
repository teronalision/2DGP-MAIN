from pico2d import *

musics, sounds = None, None
volume = None


def init():
    global musics, sounds

    musics = [load_music('Sound\OP.mp3'),load_music('Sound\\1st.mp3')]
    sounds = []


def play_music(n):
    musics[n].repeat_play()

def stop_music():
    for m in musics:
        m.stop()