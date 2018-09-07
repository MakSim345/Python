# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
PAD_VELOCITY = 6
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# Calc distance
def distance(x,y,r=0):
    """
        Calculate circle distance to a given point
    """
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2) - r

def ball_side():
    """
        return LEFT or RIGHT
    """
    if ball_pos[0] > WIDTH/2:
        return RIGHT
    else:
        return LEFT
    
def can_touch_paddle():
    """
        Determine if ball can touch paddle
    """
    if ball_pos[0] < WIDTH/2:
        return (ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= paddle1_pos+PAD_HEIGHT)
    else:
        return (ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= paddle2_pos+PAD_HEIGHT)

    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240),-random.randrange(60, 180)]
    else:
        ball_vel = [-random.randrange(120, 240),random.randrange(60, 180)]
    
    # Normalize velocity
    ball_vel[0] /= 60
    ball_vel[1] /= 60

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.random()>=0.5)
    score1 = score2 = 0
    paddle1_vel = paddle2_vel = 0
    paddle1_pos = paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    
def draw_paddle(canvas, corner):
    """
        Draws paddle starting from left upper corner
    """
    p = [corner]
    p.append([corner[0],           corner[1]+PAD_HEIGHT])
    p.append([corner[0]+PAD_WIDTH, corner[1]+PAD_HEIGHT])
    p.append([corner[0]+PAD_WIDTH, corner[1]])
    canvas.draw_polygon(p, 1, "Red", "White")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if (distance(ball_pos, [ball_pos[0], 0], BALL_RADIUS) <= 0) or (distance(ball_pos, [ball_pos[0], HEIGHT], BALL_RADIUS) <= 0):
        ball_vel[1] *= -1
        
    if (distance(ball_pos, [PAD_WIDTH, ball_pos[1]], BALL_RADIUS) <= 0) or (distance(ball_pos, [WIDTH-PAD_WIDTH, ball_pos[1]], BALL_RADIUS) <= 0):
        if can_touch_paddle():
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            if ball_side() == LEFT:
                score2 += 1
                spawn_ball(RIGHT)
            else:
                score1 += 1
                spawn_ball(LEFT)
            
            
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Blue", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos < 0:
        paddle1_pos = 0
    if paddle1_pos > HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT

    paddle2_pos += paddle2_vel
    if paddle2_pos < 0:
        paddle2_pos = 0
    if paddle2_pos > HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT

    
    
    # draw paddles
    draw_paddle(canvas, [0,paddle1_pos])
    draw_paddle(canvas, [WIDTH - PAD_WIDTH, paddle2_pos])
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/2 - 60, 30], 40, "Red")
    canvas.draw_text(str(score2), [WIDTH/2 + 40, 30], 40, "Yellow")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = PAD_VELOCITY
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -vel
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = vel
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart" , new_game, 80)


# start frame
new_game()
frame.start()
