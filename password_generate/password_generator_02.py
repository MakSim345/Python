import string
import random
f = lambda x, y: ''.join([x[random.randint(0,len(x)-1)] for i in xrange(y)]); f(list(string.ascii_letters+string.digits), 12) 

print f("habrahabr", 12)

def password_generator(_str, y):
    f = list(string.ascii_letters+string.digits)
    # print f
    _result = ''
    _result2 = ""
    for i in range(y):
        a = random.randint(0, len(_str) - 1)
        # print a, 
        b = f[a]
        print b,
        #_result.join(b)
        _result = _result + b
        print "_result", _result
    return _result        

print password_generator("habrahabr", 12)
