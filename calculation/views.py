from django.http import HttpResponse
from django.shortcuts import render

from .models import Fibonacci, PiCalculation, Pythagorean

# Main page view
def main_page(request):
	
	return render(request, 'calculation/index.html')

# First calculation view (Fibonacci)
def fib(request):
	result = Fibonacci(starting_val=0)
	result.save()

	return render(request, 'calculation/fib.html', {'result': result})

# Second calculation view (Pi Approximation)
def pi(request):
	pi_string = PiCalculation()
	pi_string.save()

	return render(request, 'calculation/pi.html', {'pi_string': pi_string})

# Third calculation view (Pythagorean Theorem)
def pythagorean(request):
	hypotenuse = Pythagorean()
	hypotenuse.save()

	return render(request, 'calculation/pythagorean.html', {'hypotenuse': hypotenuse})
