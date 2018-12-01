import ENGINE
import pico2d
import TITLE


pico2d.open_canvas(800,600,True,True)

ENGINE.init()
ENGINE.Push_state(TITLE)
ENGINE.Run()
    
pico2d.close_canvas()