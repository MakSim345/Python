# http://www.codeskulptor.org/#user38_8PjolfgU0xNAQIT.py

# template for "Stopwatch: The Game"

'''
- What is best:
    - you use internal function timer.is_running(), great!
    - you set 10 minutes limit to play, very clever.
    - very nicely selected fonts and colors, easy to play;

Unfortunatelly, if I have 100+ attemps and 10+ wins, the score move out of frame.

'''

import simplegui

# define global variables
counter = 0
attempts = 0
wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = str(t % 10)
    seconds = str((t % 600) / 10)
    if len(seconds) == 1:
        seconds = '0' + seconds
    minutes = str(t / 600)
    clock = minutes + ':' + seconds + '.' + tenths
    return clock
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    if not timer.is_running():
        timer.start()

def stop_handler():
    global attempts, wins
    if timer.is_running():
        timer.stop()
        attempts += 1
        if counter % 10 == 0:
            wins += 1

def reset_handler():
    global counter, attempts, wins
    if timer.is_running():
        timer.stop()
    counter = 0
    attempts = 0
    wins = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    if counter < 6000:
        counter += 1
    else:
        counter = 0

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), (100, 110), 36, "Black")
    canvas.draw_text(str(wins) + ' / ' + str(attempts),
                     (230, 30), 24, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)

# register event handlers
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
