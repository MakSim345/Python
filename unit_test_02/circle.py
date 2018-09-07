#!/usr/bin/env python
from math import pi

def saveMessageToLog(_my_text):
    _log_file_name = 'unit_test.log'
    file = open(_log_file_name, "a")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
    file.write("Message:\n" + _my_text)
    file.write("-------------------------------------\n")
    file.close()


def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The RADIUS must be a non-negative real number")

    if r<0:
        raise ValueError("The RADIUS can not be negative.")

    return pi*(r**2)

def test_area_circle():
    #test function
    radii = [2, 0, -3, 2+5j, True, "radius"]
    message = "Area of circles wirh r = {radius} is {area}."
    for r in radii:
        print "Radius to test:", r
        A = circle_area(r)
        print message.format(radius=r, area = A)

# main entrance point:
if __name__ == "__main__":
    # n = input('Enter the positive number: ')
    # print '{0}! = {1}'.format(n, factorial(int(n)))

    # print "for Radius", n, "circle area is:", circle_area(int(n))
    test_area_circle()
