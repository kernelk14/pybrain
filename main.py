#!/usr/bin/env python3
from collections import deque
from sys import argv

# This is the program structure.
# |-- The code below is being separated through a file.
# `--           K    K-3 = H     Y           Y-13 = L   L-7 = E
# program = "++++++++++,---,++++++++++++++,-------------,-------,/"
# program = "++++++++++++++++++++++,--------,+-,/"
prog = open(argv[1], 'r')
program = prog.read().replace("\n", "")
ip = 0

alpha = "a"
stack = deque()
restore_stack = deque()
while (ip < len(program)):
    code = program[ip]
    # print(code)
    stack.append(alpha)
    if (code == "+"):
        next_alpha = chr(ord(alpha) + 1)
        stack.append(next_alpha)
        alpha = stack.pop()
        next_alpha = chr(ord(alpha) + 1)
    elif (code == "-"):
        prev_alpha = chr(ord(alpha) - 1)
        stack.append(prev_alpha)
        alpha = stack.pop()
        prev_alpha = chr(ord(alpha) - 1)
    elif (code == "."):
        a = stack.pop()
        print(a)
        alpha = a
        stack.append(alpha)
    elif (code == ","):
        a = stack.pop()
        restore_stack.append(a)
        stack.append(a)
    elif (code == "/"):
        data = "".join(restore_stack)
        print(data)
    elif (code == ";"):
        stack.clear()
        restore_stack.clear()
        alpha = "a"
    else:
        print(f"Position {ip}: Expecting `+`, `-`, `,` and `.`, but got `{code}`.")
        exit(1)
    # print(f"The restore stack: {restore_stack}") 
    # print(f"The stack: {stack}")
    ip += 1
