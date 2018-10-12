from pico2d import *



def Quit():
    global run
    run = False

def Run(state):
    global run, state_stack
    run = True

    state_stack = [state]
    state_stack.start()

    while run:
        state_stack[-1].handle()
        state_stack[-1].update()
        state_stack[-1].draw()

    while(len(state_stack)>0):
        state_stack[-1].end()
        state_stack.pop()



#초기화

run = True
state_stack


open_canvas()

#게임 본체
while True:
    get_events()


    
    clear_canvas()
    update_canvas
    delay(0.05)
    



#종료
close_canvas()
