#!/usr/bin/env python
import operator

def factorial(n):
    if n < 0:
        raise ValueError("Factorial can't be calculated for negative numbers.")
    if type(n) is float or type(n) is complex:
        raise TypeError("Factorial doesn't use Gamma function.")
    if n == 0:
        return 1
    return reduce(operator.mul, range(1, n + 1))

def saveMessageToLog(_my_text):
    _log_file_name = 'unit_test.log'
    file = open(_log_file_name, "a")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
    file.write("Message:\n" + _my_text)
    file.write("-------------------------------------\n")
    file.close()

# main entrance point:
if __name__ == "__main__":
    #print "Main program start."
    #print ""

    n = input('Enter the positive number: ')
    # print '{0}! = {1}'.format(n, factorial(int(n)))
    print "For number", n, "factorial is:"
    print factorial(int(n))

    #num = input("Weather SMS for Helsinki sent. Press Enter.\n")

    #print ""
    #print "Main program end."



