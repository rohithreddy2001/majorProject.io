from django.shortcuts import render
from django.http import HttpResponse
from hsp.forms import patientForm
from hsp.models import patientdatamodel


def hsplogin(request):
    return render(request, "hsp/hsplogin.html")

def hsploginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='hsp' and passwd=='hsp':
            return render(request,"hsp/hsploginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "hsp/hsploginentered.html")


def uploadpatientdata(request):
    if request.method == 'POST':
        form=patientForm(request.POST,request.FILES)
        file=request.POST.get('file')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        gender=request.POST.get('gender')
        weight=request.POST.get('weight')
        age=request.POST.get('age')
        symptomps=request.POST.get('symptomps')
        doctor=request.POST.get('doctor')
        print("file:",file,name,email,mobileno,gender,weight,age,symptomps,doctor)
        qs=patientdatamodel.objects.create(name=name,email=email,mobileno=mobileno,gender=gender,weight=weight,age=age,symptomps=symptomps,doctor=doctor,file=file)
        return render(request,'hsp/uploadpatientdata.html')
    else:
        form = patientForm()
        return render(request, 'hsp/uploadpatientdata.html', {"form": form})


def viewpatientdata(request):
    qs=patientdatamodel.objects.all()
    return render(request,'hsp/viewpatientdata.html',{"object":qs})












