#!/usr/bin/env python

# Number to guess: How many passwords
# can we bcrypt in a second?

import bcrypt

password = 'a' * 100

def f(NUMBER):
    for _ in range(NUMBER):
        bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        
if __name__ == '__main__':
    import sys
    f(int(sys.argv[1]))
