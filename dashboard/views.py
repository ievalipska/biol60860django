from django.shortcuts import render
from .models import Variants


def home(request):
    variants = Variants.objects.all()
    
    data = {
        'variants': variants,
    }
    return render(request, 'dashboard/home.html', {'data': data})

def addvariant(request):
    return render(request, 'dashboard/addvariant.html')
