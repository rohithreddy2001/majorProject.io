from builtins import Exception
from hsp.models import patientdatamodel
from django.shortcuts import render
from django.http import HttpResponse
from doctor.forms import doctorForm
from doctor.models import doctorModel
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def doctorlogin(request):
    return render(request,'doctor/doctorlogin.html')

def doctorregister(request):
        if request.method == 'POST':
            form1 = doctorForm(request.POST)
            if form1.is_valid():
                form1.save()
                print("succesfully saved the data")
                return render(request, 'doctor/doctorlogin.html')
                # return HttpResponse("registreration succesfully completed")
            else:
                print("form not valied")
                return HttpResponse("form not valied")
        else:
            form = doctorForm()
            return render(request, "doctor/doctorregister.html", {"form": form})

def doctorlogincheck(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        print(sname)
        spasswd = request.POST.get('upasswd')
        print(spasswd)
        try:
            check = doctorModel.objects.get(email=sname,passwd=spasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            request.session['name'] = check.name
            print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'doctor/doctorpage.html')
            else:
                messages.success(request, 'doctor is not activated')
                return render(request, 'doctor/doctorlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid name and password')
        return render(request,'doctor/doctorlogin.html')


def doctorviewpatientdata(request):
    doctor=request.session['name']
    qs=patientdatamodel.objects.filter(doctor=doctor)
    print("qs:",qs)
    return render(request,'doctor/doctorviewpatientdata.html',{"object":qs})


def addtreatment(request):
    if request.method == 'GET':
        mail=request.GET.get('mail')
        qs = patientdatamodel.objects.filter(email=mail)
        print("qs",qs)
        return render(request,'doctor/doctortreatment.html',{"object":qs})






