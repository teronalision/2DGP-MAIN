from pico2d import *
import 기본
import boot



def Quit():
    global run
    run = False

def Run(state):
    global run, state_stack
    run = True

    state_stack = [state]
    state.start()

    while run:
        state_stack[-1].handle()
        state_stack[-1].update()
        state_stack[-1].draw()


    while(len(state_stack)>0):
        state_stack[-1].end()
        state_stack.pop()



#초기화

run = True
state_stack = None


open_canvas()

#게임 본체

Run(기본)    
    



#종료
close_canvas()
