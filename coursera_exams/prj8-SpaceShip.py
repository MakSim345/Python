# program template for Spaceship

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
import random

# globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0
is_started = False
rock_group = set([])
ROCK_LIFESPAN = float('inf')

missile_group = set([])
MISSILE_LIFESPAN = 50 
MAX_ROCK_NUM = 12

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        #endif
        self.is_animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.is_animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)

ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# Ship class
class Ship:
    '''Ship'''
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
        #endif

        # remove this:
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1
        #endif

        self.vel[0] *= 0.99
        self.vel[1] *= 0.99

    def set_thrust(self, is_On):
        self.thrust = is_On
        if self.thrust:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
       #endif

    def inc_angle_vel(self):
        self.angle_vel += 0.05
        
    def dec_angle_vel(self):
        self.angle_vel -= 0.05
        
    def shoot(self):
        global missile_group
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        one_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        
        if len(missile_group) < 40: 
            missile_group.add(one_missile)   
        #endif
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        
        if sound:
            sound.rewind()
            sound.play()
        #endif

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self, lifespan): 
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height
        
        if (self.age < lifespan):
            self.age += 1
            return True 
        elif (self.age >= lifespan):
            return False 
        #endif
        
    def collide(self, other_object):
        if (self.radius + other_object.radius) > (math.sqrt((math.pow((self.pos[0] - other_object.pos[0]), 2)) + (math.pow((self.pos[1] - other_object.pos[1]), 2)))):
            return True 
        else:
            return False
        #endif    
            
def handle_sprite_group(sprite_set, canvas, lifespan):  
    ss_cpy = sprite_set
    for item in ss_cpy: 
        if item.update(lifespan) == True: 
            item.draw(canvas)
        else: 
            sprite_set.remove(item) 
        #endif
    #end_for

def group_collide(sprite_set, other_object): 
    for a_sprite in sprite_set:
        if a_sprite.collide(other_object): 
            sprite_set.remove(a_sprite) 
            return sprite_set
        #endif
    #end_for    
                   
# key handlers to control ship   
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.dec_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.inc_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.inc_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.dec_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)
        
def mouse_click(pos):
    '''handle mouse click - reset gui and conditions if splash-screen draw'''
    global is_started
    center = [width / 2, height / 2]
    size = splash_info.get_size()
    in_width = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    in_height = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    
    if (not is_started) and in_width and in_height:
        is_started = True
    #endif

def draw(canvas):
    global time 
    global rock_group
    global missile_group
    global score, lives
    font_size_s = 22
    font_size_m = 30

    # animate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    # dirty hack:
    if wtime <= 0:
        wtime = wtime + 1

    #draw nebula:
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    
    #draw slow movement stones:
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])

    # print game info on screen:
    canvas.draw_text("Lives",    [50, 50], font_size_s, "White")
    canvas.draw_text(str(lives), [50, 80], font_size_m, "White")
    
    canvas.draw_text("Score",    [680, 50], font_size_s, "White")
    canvas.draw_text(str(score), [680, 80], font_size_m, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    
    handle_sprite_group(rock_group, canvas, ROCK_LIFESPAN) 
    
    for rock in rock_group: 
        if rock.collide(my_ship):
            group_collide(rock_group, my_ship)
            if lives == 1: 
                # game over. 
                reset()
            else: 
                lives -= 1
            #endif
        #endif
    #end_for    
            
    handle_sprite_group(missile_group, canvas, MISSILE_LIFESPAN) 
    
    for missile in missile_group: 
        for rock in rock_group: 
            if missile.collide(rock):
                group_collide(rock_group, missile) 
                score += 1
            #endif
        #end_for    
    #end_for    
    
    # update ship and sprites
    my_ship.update()

    # draw splash screen if not started
    if (not is_started):
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [width/2, height/2], 
                          splash_info.get_size())
    #endif

def rock_spawner():
    '''timer handler that spawns a rock'''
    global rock_group, my_ship
    rock_pos = [random.randrange(0, width), random.randrange(0, height)]
    rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    rock_avel = random.random() * .2 - .1
    a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
    
    if len(rock_group) < MAX_ROCK_NUM and not a_rock.collide(my_ship): 
        rock_group.add(a_rock)  
    #endif

def reset(): 
    '''initialize ship and sprites'''
    global is_started
    global time, my_ship, rock_group, missile_group, lives, score
    
    my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)
    rock_group = set([])
    missile_group = set([])
    is_started = False
    time = 0
    score = 0 
    lives = 3

# main entrance point:
if __name__ == "__main__":
    print "Main app start"

    # initialize all:
    frame = simplegui.create_frame("Asteroids", width, height)

    reset()
    # register handlers
    frame.set_keyup_handler(keyup)
    frame.set_keydown_handler(keydown)
    frame.set_mouseclick_handler(mouse_click)
    frame.set_draw_handler(draw)

    timer = simplegui.create_timer(1000.0, rock_spawner)

    # get things rolling
    timer.start()
    frame.start()
    
    print "Main app end."


