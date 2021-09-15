## Aleksandar Vranjes
## 301290015

# Project Overview

The overall goal of this project is to showcase some calculations on a webpage, using Python's Django framework to display the information but using other
programming languages to do the actual mathematical processing.

I used Python for the web framework (Django), C++ for the Fibonacci Sequence page data, Java for the Pi Approximation page data, and Go for the Pythagorean Theorem page data.
All external scripts can be found in the calculation/scripts/ directory.

# Steps to get started
See the file README.md to find the list of commands to get the project up and running.

# Subprocess Coding

To communicate between Python, C++, and Java, I used the subprocess module in Python. This allows you to run an executable (fib for C++ and Pi.jar for Java)
while in Python, then capture and use the standard output however you see fit.

For the Fibonacci Sequence page, the C++ code used is in fib.cpp and it is pre-compiled to fib. You can compile it again yourself with the command (in calculation/scripts/):

	$ g++ -o fib fib.cpp

Then run with:

	$ ./fib

The models.py code runs the code from outside the directory with the following command (in calculation/scripts/):

	$ ./calculation/scripts/fib

For the Pi Approximation page, the Java code is used in Pi.java and is also pre-compiled to a .jar file. You can compile it again with these commands (in calculation/scripts/):

	$ javac Pi.java
	$ jar -cvf Pi.jar Pi.class

The models.py code runs the code with the following command:

	$ java -cp ./calculation/scripts/Pi.jar Pi

# Foreign Function Interface

To communicate between Go and Python, I used the ctypes library to export functions from Go to be used in Python. The functions, like with fib.cpp and Pi.jar, are already
exported, but to export them again use the following command (in calculation/scripts/):

	$ go build -o pythagorean.so -buildmode=c-shared pythagorean.go

This exports functions used in pythagorean.go to be accessed in models.py in the Django framework.


