#!/usr/bin/env python

# Number to guess: How many bytes can we write
# to a string in memory in a second?

import io

CHUNK_SIZE = 1000000
s = "a" * CHUNK_SIZE

def f(NUMBER):
    output = io.BytesIO()
    bytes_written = 0
    while bytes_written < NUMBER:
        output.write(s.encode("utf8"))
        bytes_written += CHUNK_SIZE

if __name__ == '__main__':
    import sys
    f(int(sys.argv[1]))
