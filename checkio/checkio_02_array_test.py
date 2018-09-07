import os
import sys

def my_checkio(els):
    a = [] # new array
    comm_arr = [] # new array
    ret_arr = [] # new array
    for b in els:
        if b in a:
            comm_arr.append(b)
        else:
            a.append(b)
    # print "array a: ", a
    for c in els:
        if c in comm_arr:
            ret_arr.append(c)
        else:
            pass
    print "ret_arr: ", ret_arr
    return ret_arr

def checkio_3(els):
    return [i for i in els if els.count(i) > 1]


def checkio(data):
    res = 0
    _mediana = (len(data)-1) / 2
    _arr = data
    _arr.sort()
    #print _arr
    #print "array has ", len(data), "items"

    if len(data)%2==0:
        _mediana = len(data) / 2
        #print "mediana:", _mediana
        #print data[_mediana-1]
        #print data[_mediana]
        res = (data[_mediana] + data[_mediana-1]) / 2.0
    else:
        #for b in data:
        #    res = res + b

        # res = res/len(data)
        res = data[_mediana]

        #print "mediana:", _mediana, "value:", data[_mediana]
    print "result:", res
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    assert checkio([1, 2, 3, 4, 5, 6, 7]) == 4, "Sorted list"
    assert checkio([1, 2, 3, 4, 5, 6]) == (4+3)/2.0, "Sorted list"
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"

    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")

    print ""
    print "Main program end."
