from django.shortcuts import render
from .models import Variants


def home(request):
    variants = Variants.objects.all()
    return render(request, 'dashboard/home.html', {'variants': variants})


def addvariant(request):
    return render(request, 'dashboard/addvariant.html')
