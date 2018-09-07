#http://www.codeskulptor.org/#user38_v3TbyfRGOFaRIdo.py
# template for "Stopwatch: The Game"

'''
Great Gob!

Some comments:
- very small fonts, hard to play;
- green score practically invisible;
- successful attempts not registered correctly. Sometimes if last digit is zero successful attempts are increasing, sometimes not. Randomly?
- after 100 clicks on "start-stop" buttons the score move out of frame, looks not good.

In code:
- "counter" and "counter1" are bad names, not self-explained.
- you should't use "time % 50" for counting the score. It doesn't work according to specs.

'''
import simplegui
# define global variables
position = [70, 100]
position1 = [160, 20]
width = 200
height = 200
time = 0
interval = 100
counter = 0
counter1 = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = int(t / 600)
    s = int(t // 10)
    b = int(s % 60 // 10)
    if (b < 10):
        strb = '0' + str(b)
    else:
        strb = str(b)
    c = int(s % 10)
    d = int(t % 10)
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global time
    timer.start()
    return time

def stop():
    global time
    global counter
    global counter1
    if(timer.is_running() and time > 0):
        timer.stop()
        if ((time % 50) == 0):
            counter += 1
            counter1 += 1
        else:
            counter1 += 1
        return counter, counter1
    
def reset():
    global time
    global counter
    global counter1
    timer.stop()
    time = 0;
    counter = 0
    counter1 = 0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
   
       
# define draw handler
def draw(canvas):
    global time
    global counter
    global counter1
    canvas.draw_text(format(time), position, 30, "White")
    canvas.draw_text(str(counter) + "/" + str(counter1), position1, 20, "Green")
    
    
# create frame
frame = simplegui.create_frame("StopWatch", width, height)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
