from pico2d import *
import main

image = None

def start():
    global image
    image = load_image('test.png')


def end():
    global image
    del(image)


def handle():
    events = get_events()

    for e in events:
        if(e.type == SDL_QUIT):
            main.Quit()


def update():
    delay(0.1)


def draw():
    clear_canvas()

    image.draw(400,300)


    update_canvas()