# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

upper_range_limit = 101
number_to_guess = random.randrange(0, upper_range_limit, 1.0)
guess_count = 0

# helper function to start and restart the game
def new_game():
    global guess_count
    guess_count = int(math.log(upper_range_limit, 2) + 1)
    print "Range is 0:" + str(upper_range_limit - 1) + "."
    print "You have " + str(guess_count) + " guesses remaining."
    print

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global upper_range_limit
    upper_range_limit = 101
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global upper_range_limit
    upper_range_limit = 1001
    new_game()
    
def input_guess(guess):
    global guess_count
    import sys
    try:         
       if float(guess) == number_to_guess:
           print 'You win! The number was ' + str(number_to_guess) + "."
           print
           print 'New Game!'
           new_game()
       elif guess_count - 1 == 0: 
           print 'Sorry you lose. You have no remaining guesses'
           print
           print 'New Game!'
           new_game()
       elif float(guess) > number_to_guess and guess:
           guess_count -= 1
           print 'Your guess was: ' + guess
           print 'That is not the number. Lower'
           print 'You have ' + str(guess_count) + ' remaining.'
           print
       elif float(guess) < number_to_guess:
           guess_count -= 1
           print 'Your guess was: ' + guess
           print 'That is not the number. Higher'
           print 'You have ' + str(guess_count) + ' remaining.'
           print
    except ValueError:
        print 'Sorry that wasn\'t a valid number. Please try again.'
def draw_handler(canvas):
    canvas.draw_text('Welcome to the Number Guessing Game', 
                     (20, 50), 18, 'red')
    canvas.draw_text('To play: enter your first guess and hit enter.', 
                     (20, 100), 18, 'red')
    canvas.draw_text('Click on buttons to start new game.',
                     (20, 150), 18, 'red')
    canvas.draw_text('Enjoy!!!', (20, 200), 18, 'red')
# create frame
frame = simplegui.create_frame('Guess the number game', 400, 300)

# register event handlers for control elements and start frame
frame.add_button('New game: range 0:100', range100, 200)
frame.add_button('New game: range 0:1000', range1000, 200)
frame.add_input('Take your guess', input_guess, 200)
frame.set_canvas_background('White')
frame.set_draw_handler(draw_handler)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
