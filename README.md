# brainfuck-interpreter

Based off of/ported from (with some improvements) [Thomas Cort's BFI](http://esoteric.sange.fi/brainfuck/impl/interp/BFI.c).

This is a simple brainfuck interpreter that runs BF scripts and boasts a somewhat limited interactive interpreter, written in python.
It clings very loosely to the "standard" brainfuck rules, with some exceptions, as outlined below.

[This](https://esolangs.org/wiki/Brainfuck) site was pretty helpful.

**Loads of fun stuff [here](http://esoteric.sange.fi/brainfuck/).**

## Usage
> ./bfi.py \[--repl\] \[--file \<file\>\]

In repl mode, 'exit' may be typed in the console to exit (duh).

## Limitations
* In repl mode the arrow keys will not move the cursor.
* By default, the '.' will print the ascii equivalent of the value under the tape pointer.
	* This can be changed by editing line 49 in bfi.py, by removing the chr() function and its corresponding parentheses.
	* Note: ',' will still convert the first character of input to its ascii equivalent.

## REPL Prompts
In repl mode, the BF prompt looks like
> (0|0)\> 

with the current tape pointer position and value of the current cell in parentheses.

And the input prompt (invoked by ',') being
> \> 

Note: I have changed the way characters are stored on the tape. Instead of storing chars as Python string objects it will store their ascii decimal equivalents. The same applies to printing the values in cells - the value will be converted to its ascii equivalent. Look in Limitations for info on how to change this. I made this change to make my interpreter work more like Thomas Cort's BFI.
