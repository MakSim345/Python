'''
Turn the following English description into code:
- Create a list with two numbers, 0 and 1, respectively.
- For 40 times, add to the end of the list 
  the sum of the last two numbers.

What is the last number in the list?

To test your code, if you repeat 10 times, rather than 40, 
your answer should be 89.

'''

def quizz5a():
    x = 0
    y = 1
    for i in range(40):
        x, y = y, x + y
    print y


def quizz5a_my(_max_val):    
    res = 0
    a = [0, 1]
    b = []
    for i in range (_max_val):    
        # print i
        res = a[i] + a[i+1]
        a.append(res)
        # print "a", a
    
    print "result for", _max_val, " = ",  a[-1]   

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    # quizz5a_my(10)
    quizz5a_my(40)
    print "Main program end."

