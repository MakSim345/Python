# template for "Stopwatch: The Game"

import simplegui
'''
http://www.codeskulptor.org/#user38_kvv7q3mH91_4.py

Great job! App works as requested.

Some comments:
- very small fonts, hard to play;
- green score practically invisible;
- after 100 clicks on "start-stop" buttons the score move out of frame, looks not good.
Code:
- in stop_button_handler() you have an if-else structure, where checking "is_timer_on == True" in both branches. Bad practice.
- variables name "a,c,d" are not informative. Bad practice, better to give longer names;
- variable name "integer" is easy to mix with possible reserved words, better to use "int_counter" or something;
- all global definition in a function better to compose in one block, in beginning;
'''

# define global variables

integer = 0
count_stop = 0
correct_stop = 0
is_timer_on = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

    
def format(integer):
    global d
    d = integer % 10
    c = int(integer / 10) % 60
    a = integer // 600
    if integer <= 99:
        result = "0:0" + str(c) + "." + str(d)    
        return result
    elif integer <= 599:
        result = "0:" + str(c) + "." + str(d)
        return result
    elif c < 10:
        result = str(a) + ":0" + str(c) + "." + str(d)
        return result
    else:
        result = str(a) + ":" + str(c) + "." + str(d)
        return result
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_button_handler():
    timer.start()
    global is_timer_on
    is_timer_on = True

    
def stop_button_handler():
    timer.stop()
    global is_timer_on
    global correct_stop
    global count_stop
    if is_timer_on == True and d == 0:
        count_stop += 1
        correct_stop += 1
    elif is_timer_on == True:
        count_stop += 1
    is_timer_on = False
        
    
def reset_button_handler():
    timer.stop()
    global integer
    integer = 0
    global count_stop
    count_stop = 0
    global correct_stop
    correct_stop = 0
    is_time_on = False
    
def score_board():
    score = str(correct_stop) + "/" + str(count_stop)
    return score
       
# define event handler for timer with 0.1 sec interval
def update():
    global integer
    integer += 1
    return integer

# define draw handler

def draw_handler(canvas):
    global position
    canvas.draw_text(format(integer), (115, 100), 30, "white")
    canvas.draw_text(score_board(), (250, 30), 20, "green")
    
# create frame

frame = simplegui.create_frame("Timer", 300, 200)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button('Start', start_button_handler)
stop_button = frame.add_button('Stop', stop_button_handler)
reset_button = frame.add_button('Reset', reset_button_handler)



# register event handlers

timer = simplegui.create_timer(100, update)


# start frame
frame.start()

# Please remember to review the grading rubric
