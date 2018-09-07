import os
import sys
import re
'''
Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module. The password will be considered
strong enough if its length is greater than or equal to 10 symbols, it has at least one
digit, as well as containing one uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.
Input: A password as a string (Unicode for python 2.7).
Output: Is the password safe or not as a boolean or any data type that can
be converted and processed as a boolean. In the results you will see the converted results.

Precondition:
    re.match("[a-zA-Z0-9]+", password)
    0 < len(password) <= 64
    '''

def checkio_3(els):
    return [i for i in els if els.count(i) > 1]

def checkio(password):
    res = False
    one_letter = False
    one_digit = False
    len_pass = False
    cap_letter = False
    small_letter = False

    #print ("password:", password)

    if (re.match("[a-zA-Z0-9]+", password)):
        pass
        #print "re.match=OK"
    else:
        #print ("re.match=False ")
        return False

    if (0 < len(password) <= 64):
        #print "pass len = OK"
        pass
    else:
        #print ("pass len = False ")
        return False


    if len(password) <= 9:
        pass
        #_mediana = len(data) / 2
        #print "mediana:", _mediana
        #print data[_mediana-1]
        #print data[_mediana]
        #res = (data[_mediana] + data[_mediana-1]) / 2.0
    else:
        pass
        len_pass = True
        #for b in data:
        #    res = res + b

        # res = res/len(data)
        #res = data[_mediana]

        #print "mediana:", _mediana, "value:", data[_mediana]

    for i in password:
        if str.isalpha(i):
            one_letter = True
            #print "one_letter = True for ", i
            if str.islower(i):
                small_letter = True
            else:
                cap_letter = True # at least one mast be capital leter
                # print ("cap_letter = True for ", i)
            #endif
        #endif
        else:
            one_digit = True
            #print "one_digit = True for ", i
        #endif

    #print ("one_digit = ", one_digit)
    #print ("one_letter = ", one_letter)
    #print ("len_pass = ", len_pass)
    #print ("cap_letter = ", cap_letter)
    #print ("small_letter = ", small_letter)

    if (one_digit and one_letter and len_pass and cap_letter and small_letter):
        res = True
    else:
        res = False

    print ("result:", res)
    return res


DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')

def checkio_2(data):
    """
    Return True if password strong and False if not

    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False

    if not DIGIT_RE.search(data):
        return False

    if not UPPER_CASE_RE.search(data):
        return False

    if not LOWER_CASE_RE.search(data):
        return False

    return True

#These "asserts" using only for self-checking and not necessary for auto-testing

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
      #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('QWERTY911AA') == False, "7th example"
    assert checkio('@QwErTy911poqq') == False, "8th example"

    print("The local tests are done.")

    print ""
    print "Main program end."
