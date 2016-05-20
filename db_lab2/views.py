from django.shortcuts import render
from .class_db import MyDataDase
from django.http import HttpResponseRedirect

from .forms import IdForm

db = MyDataDase()

def all_posts(request):
    emp = db.ShowAllInfo()
    return render(request, 'DB_LAB2/all_posts.html', {'emp': emp})

def click(request):
    emp = db.ShowTableEmployeeInfo()
    return render(request, 'DB_LAB2/all_posts.html', {'emp': emp})

def showcompanies(request):
    emp = db.ShowTableCompanies()
    return render(request, 'DB_LAB2/ShowCompanies.html', {'emp': emp})

def showallinfo(request):
    emp = db.ShowAllInfo()
    return render(request, 'DB_LAB2/ShowAllInfo.html', {'emp': emp})

def showemployeeinfo(request):
    emp = db.ShowTableEmployeeInfo()
    return render(request, 'DB_LAB2/ShowEmployeeInfo.html', {'emp': emp})

def showworkplace(request):
    emp = db.ShowTableWorkPlace()
    return render(request, 'DB_LAB2/ShowWorkPlace.html', {'emp': emp})

def accounting(request):
    emp = db.Accounting()
    return render(request, 'DB_LAB2/Accounting.html', {'emp' : emp})

def addvisiting(request):
    if request.method == "POST":
        if request.POST["employee_id"] != "" and request.POST["date"] != "":
            db.AddVisiting(request.POST)
            emp = db.Accounting()
        return render(request, 'DB_LAB2/Accounting.html', {'emp': emp})
