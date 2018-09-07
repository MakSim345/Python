# Implementation of classic arcade game Pong

'''
Well done.
- You forget to implement the Reset button
- ball initial movement is not related to winner/looser; in "spawn_ball(direction)" the 'direction' is not in use at all;
- paddles shall be filled with a color, because it is pretty hard to see 'em.
- score is hard to see because of small fonts;
- this line "paddle1_vel = -1 * paddle_vel" is equal to "paddle1_vel = -paddle_vel", simple math....

'''

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0,0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle_vel = 10
paddle1_vel = 0
paddle2_vel = 0
left_score = 0
right_score = 0
vel = 3

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    ball_vel = [0, 0]
    ball_vel[0] = vel
    ball_vel[1] = vel
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    direction = [0, 0]
    direction[0] = random.randrange(-10.0, 10.0)
    direction[1] = random.randrange(-10.0, 10.0)
    spawn_ball(direction)

def draw(canvas):
    global left_score, right_score, paddle1_pos, paddle2_pos, ball_pos, ball_vel
       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
   
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        # determine if hit the left pad
        if (ball_pos[1] < paddle1_pos - PAD_HEIGHT/2) or (ball_pos[1] > paddle1_pos + PAD_HEIGHT/2):
            right_score +=1
            new_game()
        else:
            ball_vel[0] = -1 * ball_vel[0]
        
    elif (ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH)):
        # determine if hit the left pad
        if (ball_pos[1] < paddle2_pos - PAD_HEIGHT/2) or (ball_pos[1] > paddle2_pos + PAD_HEIGHT/2):
            left_score +=1
            new_game()
        else:
            ball_vel[0] = -1 * ball_vel[0]
    elif (ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -1 * ball_vel[1]
    elif (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = -1 * ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS/2, BALL_RADIUS, 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    temp = paddle1_pos + paddle1_vel
    if (temp >=  PAD_HEIGHT/2) and (temp <= HEIGHT-PAD_HEIGHT/2):
        paddle1_pos = temp
    
    temp = paddle2_pos + paddle2_vel
    if (temp >=  PAD_HEIGHT/2) and (temp <= HEIGHT-PAD_HEIGHT/2):
        paddle2_pos = temp
    
    # draw paddles
    # draw left paddles
    canvas.draw_line([0, paddle1_pos - PAD_HEIGHT/2],[PAD_WIDTH, paddle1_pos - PAD_HEIGHT/2], 1, "White")
    canvas.draw_line([0, paddle1_pos + PAD_HEIGHT/2],[PAD_WIDTH, paddle1_pos + PAD_HEIGHT/2], 1, "White")
    
    # draw right paddles
    canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos - PAD_HEIGHT/2],[WIDTH, paddle2_pos - PAD_HEIGHT/2], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT/2],[WIDTH, paddle2_pos + PAD_HEIGHT/2], 1, "White")
    
    # draw scores
    canvas.draw_text(str(left_score) + " : " + str(right_score), [WIDTH/2 - 16, 50], 18, 'Red')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W'] :
        paddle1_vel = -1 * paddle_vel
    
    if key == simplegui.KEY_MAP['S'] :
        paddle1_vel = paddle_vel
        
    if key == simplegui.KEY_MAP['up'] :
        paddle2_vel = -1 * paddle_vel
    
    if key == simplegui.KEY_MAP['down'] :
        paddle2_vel = paddle_vel
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W'] :
        paddle1_vel = 0
    
    if key == simplegui.KEY_MAP['S'] :
        paddle1_vel = 0
        
    if key == simplegui.KEY_MAP['up'] :
        paddle2_vel = 0
    
    if key == simplegui.KEY_MAP['down'] :
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
