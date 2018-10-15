


x, y = 0, 0
vx, vy = 0, 0
live = True


def update():
    global x,y

    if live == False:
        return

    x += vx
    y += vy