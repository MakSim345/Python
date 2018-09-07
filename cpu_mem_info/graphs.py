def graph(coords):
    x_range = 80
    y_range = 40
    x_hi = 0
    x_lo = 0
    y_hi = 0
    y_lo = 0
    output = [["`" for row in range(x_range+1)] for col in range(y_range+1)]
    for i in range(len(coords)):
        x = coords[i][0]
        y = coords[i][1]
        if x > x_hi:
            x_hi = x
        elif x < x_lo:
            x_lo = x
        if y > y_hi:
            y_hi = y
        elif y < y_lo:
            y_lo = y
    x_scale = x_range / (x_hi-x_lo)
    y_scale = y_range / (y_hi-y_lo)
    x_offset = int(x_scale * x_lo)
    y_offset = int(y_scale * y_lo)
    for i in range(len(output)):
        output[i][0-x_offset] = "|" 
    for i in range(len(output[0])):
        output[0-y_offset][i] = "-" 
    for i in range(len(coords)):
        x = int(coords[i][0]*x_scale)
        y = int(coords[i][1]*y_scale)
        output[y-y_offset][x-x_offset] = "*"
    output.reverse()
    for i in range(len(output)):
        print_row = ""
        for j in range(len(output[0])):
            print_row += output[i][j]
        print print_row

def run(param1, param2, param3):
    coords = []
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 100
    myrobot.set_steering_drift(10.0 / 180.0 * pi) # 10 degree bias, this will be added in by the move function, you do not need to add it below!
    #
    # Enter code here
    #
    CTE = myrobot.y
    intCTE = 0
    for i in range(N):
        diffCTE = myrobot.y - CTE
        intCTE += myrobot.y
        CTE = myrobot.y
        steering = -param1 * CTE - param2 * diffCTE - param3 * intCTE
        #print "steering", steering
        myrobot = myrobot.move(steering, speed)
        print myrobot, steering
        coords.append([myrobot.x, myrobot.y])

    return coords

# Call your function with parameters of (0.2, 3.0, and 0.004)
# run now returns coords list instead to allow graphing
#coords = run(0.2, 3.0, 0.004)
#coords = run(0, 3.0, 0.004)
coords = run(0.2, 0.0, 0.004)
graph(coords)