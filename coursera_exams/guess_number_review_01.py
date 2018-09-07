# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

secret_number = 0
num_range = 100
guess_number = 0
num_of_guess = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    global num_range
    global num_of_guess
    
    secret_number = random.randrange(num_range)
    num_of_guess = int(math.ceil(math.log(num_range,2)))
  
    print "New game, Range is from 0 to", num_range
    print "Number of remaining guess is", num_of_guess, "\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def get_input(guess):
    global guess_number
    guess_number = int(guess)
    input_guess()
    
def input_guess():
    # main game logic goes here 
    global guess_number
    global num_of_guess
    global secret_number
    global num_range
    correct = 0
    
    if num_of_guess > 0 and correct == 0 :
        num_of_guess -= 1
        
        print "Guess was", guess_number
        print "Number of remaining guesses is", num_of_guess
    
        if guess_number > secret_number:
            print "Lower!\n"
        elif guess_number < secret_number:
            print "Higher!\n"
        else:
            correct = 1
            
    if correct == 1:
        print "Correct!\n"
        new_game()
    elif num_of_guess == 0:
        print "You ran out of guess. The number was", secret_number, "\n"
        new_game()
        

    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric


Great job.
Especially I like how do u calculate number of guesses, based on given range. Hight math, thought...

Some comments:
in code :
------------
if correct == 1:
    print "Correct!\n"
    new_game()
elif num_of_guess == 0:
    print "You ran out of guess. The number was", secret_number, "\n"
    new_game()
-------
you call "new_game()" in both cases, so it can be moved out of if-elif structure.
-----
the variable named "correct" is obviously a flag, so it may be boolean as well, matter of taste:-)
-----
also, this if-elif structure has really strange logic, not very obvious.

BR,