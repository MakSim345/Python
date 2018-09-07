# argparse1.py
import argparse
import sys

def test_01():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", nargs=1)
    args = parser.parse_args()
    
    print "Result:",  args.a
    
    if args.a == 23:
        print 'You nailed it!'

def test_02():
    parser = argparse.ArgumentParser(description='An awesome program')
    parser.add_argument('first_name')
    parser.add_argument('last_name')
    args = vars(parser.parse_args())
    print "{} {}".format(args['first_name'], args['last_name'])

def simple_arg_parser():
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    for arg in sys.argv:
        print arg

if __name__ == '__main__':
    # test_01()   
    test_02()

    
    
    

