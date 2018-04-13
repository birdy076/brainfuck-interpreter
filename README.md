# brainfuck-interpreter

Baseed off of/ported from (with some improvements) [Thomas Cort's BFI](http://esoteric.sange.fi/brainfuck/impl/interp/BFI.c).

This is a simple brainfuck interpreter that runs BF scripts and boasts a somewhat limited interactive interpreter, written in python.
It clings very loosely to the "standard" brainfuck rules, with some exceptions, as outlines below.
*Note: This was just a fun little evening project, so there is a LOT of room for improvement - which I hope to do sometime.*

[This](https://esolangs.org/wiki/Brainfuck) site was pretty helpful.

**Loads of fun stuff [here](http://esoteric.sange.fi/brainfuck/)**

## Usage
> ./bfi.py \[--repl\] \[--file \<file\>\]

In repl mode, 'exit' may be typed in the console to exit (duh).

## Limitations
* Tape size is set to 300 by default - change the tapesize variable if you want something different
* After assigning cells with chars using the ',' command, you will not be able to increment or decrement them. The exception to this is if the char is a number.

## REPL Prompts
In repl mode, the BF prompt looks like
> (0)\> 
with the current tape pointer position in  parentheses.
And the input prompt (invoked by ',') being
> input\> 

## TODO
* Store chars as their decimal equivalents (i.e. unicode decimal values), as opposed to Python's string objects. This will allow programs to print chars without input.
