from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
	
	# Main page to show the options of calculations
    path('', views.main_page, name='main_page'),

    # First calculation page (Fibonacci in C++)
    path('fib', views.fib, name='fib'),

    # Second calculation page (Pi Approximation in Java)
    path('pi', views.pi, name='pi'),

    # Third calculation page (Pythagorean Theorem in Go)
    path('pythagorean', views.pythagorean, name='pythagorean')
]