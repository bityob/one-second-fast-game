#!/usr/bin/env python

# Number to guess: How many times can we
# download google.com in a second?

from urllib.request import urlopen


def f(NUMBER):
    for _ in range(NUMBER):
        r = urlopen("http://google.com")
        r.read()

if __name__ == '__main__':
    import sys
    f(int(sys.argv[1]))
