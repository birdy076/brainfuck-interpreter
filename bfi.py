#!/usr/bin/env python3
# brainfuck-interpreter by bloodf3ther #

import sys

src = False
buff = []  # the buffer into which will be loaded the sanitized tokens
tapelen = 30000  # length of the tape
tape = [0 for x in range(0, tapelen)]  # generates the tape
pointer = 0  # tape pointer
execptr = 0  # instruction pointer, used with buff

for arg in sys.argv:
    if len(sys.argv) < 2:
        print('Usage:\n--repl          Launches bfi in interactive mode.\n--file <file>   Executes BF code from a file.')
        sys.exit()
    elif sys.argv[1] == '--repl':  # leaves src as False - for interactive repl mode
        pass
    elif sys.argv[1] == '--file':
        try:
            src = open(sys.argv[2], 'r').read()
        except FileNotFoundError:
            print('[!] Error opening file: {0}'.format(sys.argv[2]))
            sys.exit()


def buffstuff(stuff):  # sanitizes code and populates the buffer
    global buff
    for token in stuff:
        if token in ['<', '>', ',', '.', '+', '-', '[', ']']:
            buff.append(token)
        else:
            pass  # every non command character is ignored


def evaluate():  # evaluates contents of the code buffer and does things accordingly
    global buff, tape, pointer, execptr
    brackstack = 0  # stack for matching brackets
    while execptr < len(buff):
        if buff[execptr] == '<':  # '<' moves the pointer one cell to the left
            pointer -= 1
        elif buff[execptr] == '>':  # '>' moves the pointer one cell to the right
            pointer += 1
        elif buff[execptr] == '+':  # '+' increments the cell under pointer by one
            tape[pointer] += 1
        elif buff[execptr] == '-':  # '-' decrements the cell under pointer by one
            tape[pointer] -= 1
        elif buff[execptr] == '.':  # '.' prints the value of the cell under pointer
            print(chr(tape[pointer]), end='')  # converts the decimal under pointer to char and prints it
            '''if src is False:
                print('\n')'''
        elif buff[execptr] == ',':  # ',' will store a value in the cell under pointer from user input
            tape[pointer] = ord(input('> ')[0])  # stores first char of input as decimal
        elif buff[execptr] == '[':  # '[' will jump past the matching ']' if value under pointer is zero
            if tape[pointer] == 0:
                execptr += 1
                brackstack += 1
                while brackstack > 0:
                    if buff[execptr] == '[':
                        brackstack += 1
                    if buff[execptr] == ']':
                        brackstack -= 1
                    execptr += 1
        elif buff[execptr] == ']':  # ']' will jump to the previous matching ']' if the value under the pointer is nonzero
            if tape[pointer] != 0:
                execptr -= 1
                brackstack += 1
                while brackstack > 0:
                    if buff[execptr] == '[':
                        brackstack -= 1
                    if buff[execptr] == ']':
                        brackstack += 1
                    execptr -= 1
        else:
            print('[!] Error: Invalid Token {0}'.format(buff[execptr]))
        execptr += 1


if src is not False:  # if a file was specified and found this will parse, load to buffer, and execute it before exiting
    buffstuff(src)
    evaluate()

elif src is False:  # repl mode
    print('Brainfuck Interpreter')
    while True:
        x = input('({0}|{1})> '.format(pointer, tape[pointer]))
        if x == 'exit':  # the wonderful exit command
            sys.exit()
        buffstuff(x)
        evaluate()
