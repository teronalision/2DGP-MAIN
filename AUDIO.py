from pico2d import *

musics, sounds = None, None
select = -1
volume = 100


def init():
    global musics, sounds, select

    musics = [load_music('Sound\OP.mp3'),load_music('Sound\\1st.mp3')]
    sounds = []
    select = -1



def play_music(n):
    global select
    musics[n].repeat_play()
    select = n


def stop_music():
    musics[select].pause()