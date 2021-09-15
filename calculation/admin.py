from django.contrib import admin

from .models import Fibonacci
from .models import PiCalculation
from .models import Pythagorean

admin.site.register(Fibonacci)
admin.site.register(PiCalculation)
admin.site.register(Pythagorean)
