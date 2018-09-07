import unittest
from main import factorial

class TestFactorial(unittest.TestCase):
# class TestFactorial():

    #def __init__(self, _string = "nnm"):
    #    ''' init function'''
        #self._testMethodDoc="none"
        #self._testMethodName="test_negative"

    def setUp(self):
        self.seq = range(10)

    def test_calculation(self):
        print "\n1. - Test that for number 720 factorial is 6"
        self.assertEqual(720, factorial(6))

    def test_negative(self):
        print "\n2. - Test negative factorial"
        self.assertRaises(ValueError, factorial, -1)

    def test_float(self):
        print "\n3. - Test float number factorial"
        self.assertRaises(TypeError, factorial, 1.25)

    def test_zero(self):
        print "\n4. - Test ZERO factorial"
        self.assertEqual(1, factorial(0))

# main entrance point:
if __name__ == "__main__":

    print "Main program start."
    #print ""
    # import nose
    # nose.main()
    unittest.main()
    #print ""
    print "Main program end."
