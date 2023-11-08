from django.shortcuts import render
from .models import Patient


def home(request):
    patients = Patient.objects.all()
    
    data = {
        'patients': patients,
    }
    return render(request, 'dashboard/home.html', {'data': data})

def addvariant(request):
    return render(request, 'dashboard/addvariant.html')
