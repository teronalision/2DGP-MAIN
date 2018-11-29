from pico2d import *

musics, se = None, None
select = -1
bgm_volume = 100
se_volume = 100


def init():
    global musics, se, select

    musics = [load_music('Sound\OP.mp3'),load_music('Sound\\1st.mp3'),load_music('Sound\\2nd.mp3'),load_music('Sound\\3rd.mp3')]
    se = [load_wav('Sound\se_select.wav'),load_wav('Sound\se_dead.wav'),load_wav('Sound\se_cardget.wav'),
          load_wav('Sound\se_tan00.wav'),load_wav('Sound\se_tan01.wav'),load_wav('Sound\se_tan02.wav')]
    select = -1

    #
    for m in musics:
        m.play()
        m.pause()


def play_se(n):
    se[n].play()

def play_music(n):
    global select
    musics[n].repeat_play()
    select = n


def stop_music():
    musics[select].pause()

def set_volume():
    for m in musics:
        m.set_volume(bgm_volume)
def set_SEvolume():
    for s in se:
        s.set_volume(se_volume)