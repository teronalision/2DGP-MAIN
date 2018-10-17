from pico2d import *


x, y = 0, 0
w, h = 0, 0
speed = 0.4
live = True


def update():
    global x,y

    if live == False:
        return

    if x +w*speed +40 < 500 and x +w*speed -40 > 0:
        x += w*speed
    if y +h*speed +60 < 600 and y +h*speed -60 > 0:
        y += h*speed

def handle(type, key):
    global w,h

    if type == SDL_KEYDOWN:
        if key == SDLK_LEFT:
            w = -1
        elif key == SDLK_RIGHT:
            w = 1
        if key == SDLK_UP:
            h = 1
        elif key == SDLK_DOWN:
            h = -1
    elif type == SDL_KEYUP:
        if key == SDLK_LEFT:
            w = 0
        elif key == SDLK_RIGHT:
            w = 0
        if key == SDLK_UP:
            h = 0
        elif key == SDLK_DOWN:
            h = 0