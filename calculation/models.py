# Subprocess to use C++, Java executable results in Python
import subprocess

import datetime

from django.db import models
from django.utils import timezone

# Foreign Function Interface for Go files
from ctypes import *

# The class for the first page of calculations: Fibonacci
class Fibonacci(models.Model):
	starting_val = models.IntegerField()

	def calculateSequence(self):
		'''
		Captures stdout from the fib executable (compiled from fib.cpp) and returns it to
		be used in the appropriate webpage.
		'''
		result = subprocess.run('./calculation/scripts/fib', shell=True, stdout=subprocess.PIPE)
		result_string = result.stdout.decode('utf-8')
		return result_string

# The class for the second page of calculations: Pi Approximation
class PiCalculation(models.Model):
	def calculatePiApproximation(self):
		'''
		Captures stdout from the Pi.Class file (compiled from Pi.java) and returns it to
		be used in the appropriate webpage.
		'''
		pi_sequence = subprocess.run('java -cp ./calculation/scripts/Pi.jar Pi', shell=True, stdout=subprocess.PIPE)
		pi_string = pi_sequence.stdout.decode('utf-8')
		return pi_string

# The class for the second page of calculations: Pythagorean Theorem
class Pythagorean(models.Model):
	def smallHypotenuse(self):
		'''
		Load smallTriangle() function from pythagorean.go, format return type, and return the hypotenuse
		'''
		lib = cdll.LoadLibrary("./calculation/scripts/pythagorean.so")
		lib.SmallTriangle.restype = c_double
		s_hypotenuse = lib.SmallTriangle()
		return s_hypotenuse

	# Load mediumTriangle function from pythagorean.go... etc
	def mediumHypotenuse(self):
		'''
		Load mediumTriangle() function from pythagorean.go, format return type, and return the hypotenuse
		'''
		lib = cdll.LoadLibrary("./calculation/scripts/pythagorean.so")
		lib.MediumTriangle.restype = c_double
		m_hypotenuse = lib.MediumTriangle()
		return m_hypotenuse

	# Load largeTriangle function from pythagorean.go... etc
	def largeHypotenuse(self):
		'''
		Load largeTriangle() function from pythagorean.go, format return type, and return the hypotenuse
		'''
		lib = cdll.LoadLibrary("./calculation/scripts/pythagorean.so")
		lib.LargeTriangle.restype = c_double
		l_hypotenuse = lib.LargeTriangle()
		return l_hypotenuse

	# Load extraLargeTriangle function from pythagorean.go... etc
	def extraLargeHypotenuse(self):
		'''
		Load extraLargeTriangle() function from pythagorean.go, format return type, and return the hypotenuse
		'''
		lib = cdll.LoadLibrary("./calculation/scripts/pythagorean.so")
		lib.ExtraLargeTriangle.restype = c_double
		xl_hypotenuse = lib.ExtraLargeTriangle()
		return xl_hypotenuse