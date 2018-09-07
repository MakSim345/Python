import unittest
import random
import string
import ord_lib

class checkStringFunctions(unittest.TestCase):
    def testOrd(self):
        rand_char = random.choice(string.letters)
        rand_char_ord = ord_lib.get_ord(rand_char)
        print rand_char_ord

        self.assertEqual(rand_char, rand_char)

        #new_char = random.choice(string.letters)
        #self.assertEqual(rand_char, new_char)



class checkNumbers(unittest.TestCase):
    def testInt(self):
        self.assertEqual(2, 2)


# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""

    unittest.main()

    print ""
    print "Main program ends"


