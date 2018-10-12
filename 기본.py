from pico2d import *


image = None

def start():
    global image
    image = load_image('test.png')


def end():
    global image
    del(image)


def handle():
    get_events()


def update():
    delay(0.1)


def draw():
    clear_canvas()

    image.draw(400,300)


    update_canvas()