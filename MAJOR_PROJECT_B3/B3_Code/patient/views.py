from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from patient.models import *
from patient.forms import *
from builtins import Exception
from django.contrib import messages


def patientlogin(request):
    return render(request,'patient/patientlogin.html')

def patientregister(request):
        if request.method == 'POST':
            form1 =patientForm(request.POST)
            if form1.is_valid():
                form1.save()
                print("succesfully saved the data")
                return render(request, 'patient/patientlogin.html')
            else:
                print("form not valied")
                return HttpResponse("form not valied")
        else:
            form = patientForm()
            return render(request, "patient/patientregister.html", {"form":form})

def treatment(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        symp=request.POST.get('symp')
        treatment=request.POST.get('treatment')
        patienttreatmentModel.objects.create(name=name,email=email,symptomps=symp,treatment=treatment)
        return render(request,'doctor/doctorpage.html')


def patientlogincheck(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        print(sname)
        spasswd = request.POST.get('upasswd')
        print(spasswd)
        try:
            check = patientModel.objects.get(email=sname,passwd=spasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            request.session['name'] = check.name
            print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'patient/patientpage.html')
            else:
                messages.success(request, 'patient is not activated')
                return render(request, 'patient/patientlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid name and password')
        return render(request,'patient/patientlogin.html')


def patienttreatmentresult(request):
    email=request.session['email']
    qs=patienttreatmentModel.objects.filter(email=email)
    return render(request,'patient/patienttreatmentresult.html',{"obj":qs})

