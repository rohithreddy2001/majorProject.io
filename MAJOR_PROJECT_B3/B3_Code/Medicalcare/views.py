from collections import defaultdict

from io import TextIOWrapper
import csv

from django.shortcuts import render
from django.http import HttpResponse
from patient.models import patientModel
from patient.forms import patientForm
from doctor.models import doctorModel, storedatamodel
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from django_pandas.io import read_frame
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets


def logout(request):
    return render(request, "index.html")

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='admin' and passwd=='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "admin/adminloginentered.html")

def doctordetails(request):
    qs=doctorModel.objects.all()
    return render(request,'admin/doctordetails.html',{"object":qs})

def patientdetails(request):
    qs=patientModel.objects.all()
    return render(request,'admin/patientdetails.html',{"object":qs})


def activatedoctor(request):
    if request.method == 'GET':
        uname = request.GET.get('pid')
        print(uname)
        status = 'Activated'
        print("pid=", uname, "status=", status)
        doctorModel.objects.filter(id=uname).update(status=status)
        qs = doctorModel.objects.all()
        return render(request,"admin/doctordetails.html", {"object": qs})

def activatepatient(request):
    if request.method == 'GET':
        uname = request.GET.get('pid')
        print(uname)
        status = 'Activated'
        print("pid=", uname, "status=", status)
        patientModel.objects.filter(id=uname).update(status=status)
        qs = patientModel.objects.all()
        return render(request, 'admin/patientdetails.html', {"object": qs})

def storecsvdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        csvfile =TextIOWrapper( request.FILES['file'])
        # columns = defaultdict(list)

        storecsvdata =csv.DictReader(csvfile)

        for row1 in storecsvdata:
                Pregnancies = row1["Pregnancies"]
                Glucose = row1["Glucose"]
                BloodPressure = row1["BloodPressure"]
                SkinThickness = row1["SkinThickness"]
                Insulin = row1["Insulin"]
                DiabetesPedigreeFunction = row1["DiabetesPedigreeFunction"]
                Age = row1["Age"]
                BMI = row1["BMI"]
                Outcome = row1["Outcome"]

                storedatamodel.objects.create(Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure,
                                                SkinThickness=SkinThickness, Insulin=Insulin,BMI=BMI,DiabetesPedigreeFunction=DiabetesPedigreeFunction,Age=Age,Outcome=Outcome)

        print("Name is ",csvfile)
        return HttpResponse('CSV file successful uploaded')
    else:

        return render(request, 'admin/storecsvdata.html', {})


def svm(request):

    qs = storedatamodel.objects.all()
    data = read_frame(qs)
    data = data.fillna(data.mean())
    #data[0:label]
    data.info()
    print(data.head())
    print(data.describe())
    #print("data-label:",data.label)
    dataset = data.iloc[:,[6,7]].values
    print("x",dataset)
    dataset1 = data.iloc[:,-1].values
    print("y",dataset1)
    print("shape",dataset.shape)
    X = dataset
    y = dataset1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=0)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    #print(svclassifier.predict([0.58, 0.76]))
    y_pred = svclassifier.predict(X_test)
    m = confusion_matrix(y_test, y_pred)
    accurancy = classification_report(y_test, y_pred)
    print(m)
    print(accurancy)
    x = accurancy.split()
    print("Toctal splits ", len(x))
    dict = {

        "m": m,
        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        # 'len29': x[29],
        # 'len30': x[30],
        # 'len31': x[31],
        # 'len32': x[32],
        # 'len33': x[33],

    }
    return render(request, 'admin/accuracy.html', dict)




def decision(request):

    qs = storedatamodel.objects.all()
    data = read_frame(qs)
    data = data.fillna(data.mean())
    #data[0:label]
    data.info()
    print(data.head())
    print(data.describe())
    #print("data-label:",data.label)
    dataset = data.iloc[:,[6,7]].values
    print("x",dataset)
    dataset1 = data.iloc[:,-1].values
    print("y",dataset1)
    print("shape",dataset.shape)


    dataset = datasets.load_iris()
    model = GaussianNB()
    model.fit(dataset.data, dataset.target)
    expected = dataset.target
    predicted = model.predict(dataset.data)
    accurancy = metrics.classification_report(expected, predicted)
    print("accurancy", accurancy)
    # print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    x = accurancy.split()
    print("Toctal splits ", len(x))
    dict = {

        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        'len29': x[29],
        'len30': x[30],
        'len31': x[31],
        'len32': x[32],
        'len33': x[33],


    }
    return render(request, 'admin/navieaccuracy.html', dict)