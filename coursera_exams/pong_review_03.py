# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
width = 600
height = 400       
ball_radius = 20
pad_width = 8
pad_height = 80
half_pad_width = pad_width / 2
half_pad_height = pad_height / 2
left = False
right = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is right, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [width / 2, height / 2]
    ball_vel = [0, 0]
    
    ball_vel[0] = random.randrange(120, 240) / 60
    ball_vel[1] = - random.randrange(60, 180) / 60
    
    # change only if the direction is left
    if direction == left:
        ball_vel[0] = - ball_vel[0]

# define event handlers
def new_game():
    # initialize the global variables
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    # set everything to zero
    paddle1_pos = 0
    paddle2_pos = 0
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    # every new game, start the ball to the right
    spawn_ball(right)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, right

    # top & bottom of the paddle - based on ball_radius
    boundary = math.sqrt(200)
    
    # draw mid line and gutters
    canvas.draw_line([width / 2, 0], [width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0], [pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0], [width - pad_width, height], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
        
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius - 1, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # player 1 paddle
    if paddle1_pos <= 0:
        paddle1_pos = 0
    elif paddle1_pos >= height - 1 - pad_height:
        paddle1_pos = height - 1 - pad_height
    
    # player 2 paddle
    if paddle2_pos <= 0:
        paddle2_pos = 0
    elif paddle2_pos >= height - 1 - pad_height:
        paddle2_pos = height - 1 - pad_height
        
    # draw paddles
    canvas.draw_line([half_pad_width, paddle1_pos], [half_pad_width, paddle1_pos + pad_height], pad_width, "White")
    canvas.draw_line([width - half_pad_width, paddle2_pos], [width - half_pad_width, paddle2_pos + pad_height], pad_width, "White")
    
    # draw scores
    canvas.draw_text(str(score1), [width / 4, pad_height], 40, 'White')
    canvas.draw_text(str(score2), (width * 3 / 4, pad_height), 40, 'White')

    # bounce only in 1 instance using ball_vel (Player 1)
    if ball_pos[0] <= ball_radius + pad_width and ball_pos[0] >= ball_radius + pad_width + ball_vel[0]:
        # using the paddle + distance (if top or bottom condition)
        if ball_pos[1] >= paddle1_pos - boundary and ball_pos[1] <= paddle1_pos + pad_height + boundary:
            ball_vel[0] = - ball_vel[0] * 1.1
    # start a new game
    elif ball_pos[0] <= 0:
        spawn_ball(right)
        score2 += 1
        
    # bounce only in 1 instance using ball_vel (Player 2)
    elif ball_pos[0] >= width - 1 - ball_radius - pad_width and ball_pos[0] <= width - 1 - ball_radius - pad_width + ball_vel[0]:
        # using the paddle + distance (if top or bottom condition)
        if ball_pos[1] >= paddle2_pos - boundary and ball_pos[1] <= paddle2_pos + pad_height + boundary:
            ball_vel[0] = - ball_vel[0] * 1.1
    # start a new game
    elif ball_pos[0] >= width - 1:
            spawn_ball(left)
            score1 += 1
    
    # bounce at the top
    if ball_pos[1] <= ball_radius:
        ball_vel[1] = - ball_vel[1]
    # bounce at the bottom
    elif ball_pos[1] >= height - 1 - ball_radius:
        ball_vel[1] = - ball_vel[1]
        
def keydown(key):
    global paddle1_vel, paddle2_vel

    # acceleration
    acc = 7
    # player 1 - can press both
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel = - acc
    if key == simplegui.KEY_MAP['S']:
        paddle1_vel = acc

    # player 2 - can press both
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = - acc
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = acc

def keyup(key):
    global paddle1_vel, paddle2_vel

    # player 1
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['S']:
        paddle1_vel = 0
    
    # player 2
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0   
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    
# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 150)


# start frame
new_game()
frame.start()

