# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

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

flagArrUp =0
flagArrDown =0
flagKeyUp =0
flagKeyDown =0
flagNewGame = True
flagStartFromReset = True
newGameCtr = 0
score1 = 0
score2 = 0
direction = 0

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0.0,  0.0]

paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = 0
paddle2_pos = 0

ball_speed = 60.0

def update_speed():
    global ball_vel

    ball_vel[0] += ball_vel[0] / 10.0
    
    ball_vel[1] += ball_vel[1] / 10.0    
    #ball_speed = ball_speed - 10
    # print "ball_speed=", ball_vel


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(_direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    #horisontal velosity:
    #ball_vel[0] = random.randrange(120, 240)
    #vertical velocity:
    #ball_vel[1] = random.randrange(60, 180)

    ball_vel[0] = random.randrange(120, 240) / ball_speed
    ball_vel[1] = random.randrange(60, 180) / ball_speed

    
    ball_init(_direction)

def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    print ball_vel
    if (right):
       ball_vel[0] = -ball_vel[0]
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global flagNewGame, flagStartFromReset
    global direction
    global ball_speed

    ball_speed = 60.0
    flagNewGame = True
    if flagStartFromReset:
        direction = random.randrange(0, 2)
        flagStartFromReset = False
    #else: direction already set in draw.
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global newGameCtr
    global flagNewGame
    global direction

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if (flagNewGame):    
        newGameCtr += 1
        if (newGameCtr > 15):
            flagNewGame = False
            newGameCtr = 0
    else:    
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
    
    # collide and reflect left:
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        # paddle1_pos - PAD_HEIGHT/2, paddle1_pos + PAD_HEIGHT/2
        if ( (ball_pos[1] > paddle2_pos - PAD_HEIGHT/2) and
           (ball_pos[1] < paddle2_pos + PAD_HEIGHT/2) ):
            update_speed()
        else:
            # miss hit:
            score2 += 1
            direction = 0
            new_game()

    # collide and reflect right:
    if ball_pos[0] >= (WIDTH - BALL_RADIUS) - PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        if ( (ball_pos[1] > paddle1_pos - PAD_HEIGHT/2) and
           (ball_pos[1] < paddle1_pos + PAD_HEIGHT/2) ):
            update_speed()
        else:
            # miss hit
            score1 += 1
            direction = 1
            new_game()
    
    # collide and reflect off top/bottom
    if ball_pos[1] >= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[1] <= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]        
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    step = 10
    if (flagArrDown == 1):
        paddle1_pos = paddle1_pos + step
    elif (flagArrUp == 1):
        paddle1_pos = paddle1_pos - step
    
    paddle1_pos = check_paddle_pos(paddle1_pos)

    if (flagKeyDown == 1):
        paddle2_pos = paddle2_pos + step
    elif (flagKeyUp == 1):
        paddle2_pos = paddle2_pos - step
    
    paddle2_pos = check_paddle_pos(paddle2_pos)

    # draw paddles
    canvas.draw_polyline([(0, paddle2_pos), (PAD_WIDTH, paddle2_pos)], PAD_HEIGHT, 'White')    

    canvas.draw_polyline([(WIDTH, paddle1_pos), (WIDTH-PAD_WIDTH, paddle1_pos)], PAD_HEIGHT, 'White')

    # draw scores
    canvas.draw_text(str(score1), (120, 50), 30, 'White')
    canvas.draw_text(str(score2), (460, 50), 30, 'White')

def check_paddle_pos(_new_paddle_pos):
    retVal = _new_paddle_pos

    if _new_paddle_pos >= HEIGHT - PAD_HEIGHT/2:
        retVal = HEIGHT - PAD_HEIGHT/2
    
    if _new_paddle_pos <= 0 + PAD_HEIGHT/2:
        retVal = PAD_HEIGHT/2

    return retVal    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    global flagArrUp, flagArrDown
    global flagKeyUp, flagKeyDown

    if key==simplegui.KEY_MAP["down"]:
        flagArrDown = 1        
    elif key==simplegui.KEY_MAP["up"]:
        flagArrUp = 1    
    elif key==simplegui.KEY_MAP["w"]:
        flagKeyUp = 1
    elif key==simplegui.KEY_MAP["s"]:
        flagKeyDown = 1    

def keyup(key):
    global paddle1_vel, paddle2_vel
    global flagArrUp, flagArrDown
    global flagKeyUp, flagKeyDown

    if key==simplegui.KEY_MAP["down"]:
        flagArrDown = 0
    elif key==simplegui.KEY_MAP["up"]:
        flagArrUp = 0    
    elif key==simplegui.KEY_MAP["w"]:
        flagKeyUp = 0
    elif key==simplegui.KEY_MAP["s"]:
        flagKeyDown = 0        

def onRestart():
    ''' restart buttone handler'''
    global score1, score2, flagStartFromReset
    score1 = 0
    score2 = 0
    flagStartFromReset = True
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Restart", onRestart, 200)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
