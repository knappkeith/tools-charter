import argparse

def my_thing():
    print 'hello'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=my_thing, default='yo',
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate
print args.integers