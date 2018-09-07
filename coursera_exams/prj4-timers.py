# template for "Stopwatch: The Game"

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

# define global variables
_time_counter = 0
_str_to_print = "" 
_times_of_stop = 0 
_times_of_success_stop = 0
_is_timer_run = False
_msec = 0 

#define 'constants'
timer_interval = 100
font_size_main = 90
font_size_score = 40
btn_width = 180

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(_time_to_convert):
    '''
    returns a string of the form A:BC.D where 
    A, C and D are digits in the range 0-9 
    and B is in the range 0-5.      
    format(0) = 0:00.0
    format(11) = 0:01.1
    format(321) = 0:32.1
    format(613) = 1:01.3
    '''    
    global _msec

    str_Val = ""
    # print _time_to_convert    
    _min, _sec = _divmod(_time_to_convert/10, 60)    
    _msec = (_time_to_convert - (_time_to_convert / 10) * 10)

    str_Val  = "%02d:%02d.%d" % (_min, _sec, _msec)
    
    #print _time_to_convert
    #print str_Val    
    return str_Val
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def on_start():
    ''' click handler for button Start - start timer'''    
    global _is_timer_run
    timer.start()
    _is_timer_run = True
    
def on_stop():
    ''' click handler for button stop - pause timer'''
    global _times_of_stop
    global _is_timer_run

    timer.stop()    
    # increase number of hits once per hit and only if timer running:
    if (_is_timer_run):        
        _times_of_stop += 1 
        _is_timer_run = False
        check_winner()
    #endif
    
    
def on_reset():
    ''' 
    Click handler for button reset - set all counters to zero
    Except timer itself.
    '''
    #global _time_counter
    global _str_to_print
    global _times_of_stop
    global _times_of_success_stop

    # timer.stop()
    #_time_counter = 0
    _times_of_stop = 0
    _times_of_success_stop = 0
    _str_to_print = format(_time_counter)

def total_reset():
    ''' 
    The app do not suppose to count more than 10 minutes. Here we reset all to zero
    and stop timer.
    '''
    global _time_counter
    global _str_to_print
    global _times_of_stop
    global _times_of_success_stop

    timer.stop()
    _time_counter = 0
    _times_of_stop = 0
    _times_of_success_stop = 0
    _str_to_print = format(_time_counter)
    
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(_str_to_print,  (20, 140), font_size_main, 'White')
    # make a score string with permanent width 000/000:
    str_score  = "%03d/%03d" % (_times_of_success_stop, _times_of_stop)
    canvas.draw_text(str_score, (160, 40), font_size_score, 'White')
    
# helper functions
def check_winner():    
    global _times_of_success_stop
    
    if (_time_counter == 0):
        # prevent cheating on beginning:
        return
    #endif
    
    if (_msec == 0):
        print "I C Winner!"
        _times_of_success_stop += 1
    #endif    

def _divmod(a, b):
    ''' my own implementation of a divmod function'''
    a1 = 0
    b1 = 0
    if (a == 0):
        pass
    else:            
        a1 = a / b
        if (a1 == 0):
            b1 = a
        else:
            b1 = a % b
    #endif    
    return (a1, b1)
    
# define event handler for timer with 0.1 sec interval
def on_update():
    ''' timer callback ''' 
    global _str_to_print
    global _time_counter
    _time_counter += 1
    if (_time_counter >= 6000):
        total_reset()
    #endif    
    _str_to_print = format(_time_counter)
    
# register event handlers
# create frame
frame = simplegui.create_frame('Guess the number', 300, 200)
timer = simplegui.create_timer(timer_interval, on_update)
frame.add_button("Start", on_start, btn_width)
frame.add_button("Stop", on_stop, btn_width)
frame.add_button("Reset", on_reset, btn_width)
    
frame.set_canvas_background('Blue')
frame.set_draw_handler(draw_handler)

on_reset()

# start program    
frame.start()
