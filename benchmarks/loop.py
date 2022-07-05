#!/usr/bin/env python

# Number to guess: How many iterations of an
# empty loop can we go through in a second?

def f(NUMBER):
    for _ in range(NUMBER):
        pass

if __name__ == '__main__':
    import sys
    f(int(sys.argv[1]))
