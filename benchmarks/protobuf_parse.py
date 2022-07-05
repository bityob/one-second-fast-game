#!/usr/bin/env python

import sys
sys.path.insert(0, './setup/protobuf')
from test_pb2 import TestMessage

with open('./setup/protobuf/message.protobuf') as f:
    message = f.read()

def f(NUMBER):
    for _ in range(NUMBER):
        m = TestMessage()
        TestMessage.ParseFromString(m, message)

if __name__ == '__main__':
    import sys
    f(int(sys.argv[1]))
