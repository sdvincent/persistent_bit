#!/usr/bin/env python

__authors__ = "Jared E. Stroud aka The Doc"

'''
The MIT License (MIT)

Copyright (c) 2015 sdvincent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from utilities.colors import TermColors

if __name__ == "__main__":

    cmd = ""
    print(TermColors.blue + "Goodbye World")
    while cmd !=  "exit" and cmd != "quit":

        try:
            cmd  = raw_input(">> ")

        except NameError as cerr:
            print(TermColors.red + "Sorry, I didn't understand " + str(cerr))
            print(TermColors.blue) # Go back to blue as default terminal color.
