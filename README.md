# opencv
In each numbered subdirectory there is a file labeled input.png and
another output.png. The input file corresponds to what we might get
from a camera. The output corresponds to what we'd consider to be the
important parts of the image that we'd further process.

Please write a program such that when we run it with an argument equal
to the path of the input file, it writes out a file to /tmp named
"output.png".

E.g. if we name your program "process" and run your program like so in
the shell, it should produce a file in /tmp/output.png that looks like
the sample we're giving you.

process examples/1/input.png


We'll run it on images similar to the input images. Your program
should produce images similar to the output images.

Please make sure that the longer dimension is the width and the
shorter the height. Other than that, there is no need to orient the
part.

Please use opencv (see opencv.org) to solve the problem, using either
the python or c++ library. Which to use is up to you.

If you do it in C++, please give us the program and a description of
how to compile it (or the Makefile if you're doing it that way).

E.g.

g++ foo.cpp -o  process

or "make" -- and give us the program and the Makefile(s) so we can
make it and run it.

Please give us something back we can compile and run in a Linux environment.
