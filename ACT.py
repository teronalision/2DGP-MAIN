import ENGINE
import pico2d
import TITLE


pico2d.open_canvas()

ENGINE.init()
ENGINE.Push_state(TITLE)
ENGINE.Run()
    
pico2d.close_canvas()