#!/usr/bin/env python3
from collections import deque
# This is the program structure.
# `-           K    K-3 = H     Y           Y-13 = L   L-7 = E
program = "++++++++++,---,++++++++++++++,-------------,-------,/"
# program = "++++++++++++++++++++++,--------,+-,/"
ip = 0

alpha = "a"
next_alpha = chr(ord(alpha) + 1)
stack = deque()
restore_stack = deque()
while (ip < len(program)):
    code = program[ip]
    # print(code)
    stack.append(alpha)
    if (code == "+"):
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
        print("".join(restore_stack))
    else:
        print(f"Position {ip}: Expecting `+`, `-`, `,` and `.`, but got `{code}`.")
        exit(1)
    # print(restore_stack) 
    # print(stack)
    ip += 1
