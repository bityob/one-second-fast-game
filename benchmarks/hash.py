#!/usr/bin/env python

# Number to guess: How many bytes can we md5sum in a second?

import hashlib

CHUNK_SIZE = 10000
s = 'a' * CHUNK_SIZE


def f(NUMBER):
    bytes_hashed = 0
    h = hashlib.md5()
    while bytes_hashed < NUMBER:
        h.update(s.encode("utf8"))
        bytes_hashed += CHUNK_SIZE
    h.digest()


if __name__ == '__main__':
    import sys
    f(int(sys.argv[1]))
