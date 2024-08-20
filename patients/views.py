from django.shortcuts import render
from .models import Patient

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender= request.POST.get('gender')
        disease = request.POST.get('disease')
        Patient.objects.create(name=name,gender=gender,disease=disease)

    return render(request, 'patients.html')

def patients_list(request):
    Patients = Patient.objects.all()
    return render(request, "pateints-list.html", {'Patients': Patients})