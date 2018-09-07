# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user38_JqAcBd4Q7L_3.py

'''
Well done.

Some comments:
- when timer is 0:00.0, pressing "stop" button still grow success values on the score. You haven't check this possibility.
- after "reset" score is not 0/0 really. If I press stop/start, the score restore previous game values. Not so good.
- after 10+ clicks on "start-stop" buttons the score move out of frame, looks not good. After 100+ attemps it is impossible to play.
- minutes are not show correct: after 59 it is still grow. 

In code:
- global variables name "s, m, t" are not informative. Bad practice, better to give longer names;
- names "t" and "time" - what is this? Easy to mix. Use longer names.

'''

import simplegui
import random

# define global variables
score = "0/0"
time = "0:00.0"
t = 0
s =0
m =0

def score_format(s ,m):
    return str(s)+'/'+str(m)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ms = t % 10
    t /= 10
    s = t % 60
    if s < 10:
        seconds = '0' + str(s)
    else:
        seconds = str(s)
    minute = t / 60
    return str(minute) + ':' + seconds + '.'+ str(ms)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global s, m, score
    m += 1
    if(t % 10 == 0):
        s += 1
    score = score_format(s, m)
    timer.stop()
    
def reset():
    global score, time
    m = 0
    t = 0
    s = 0
    score = score_format(s, m)
    time = format(t)
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global t, time, score, s, m
    t += 1
    time = format(t)
    score = score_format(s ,m)

# define draw handler
def draw(canvas):
    canvas.draw_text(time, [200, 250], 50, 'White')
    canvas.draw_text(score, [430, 50], 35, "Red")
    
# create frame
frame = simplegui.create_frame("StopWatch", 500, 500)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
#timer.start()

# Please remember to review the grading rubric
