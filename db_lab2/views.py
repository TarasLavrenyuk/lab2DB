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
    emps = db.ShowTableEmployeeInfo()
    if request.method == 'POST':
        info = db.GetVisitingById(request.POST['visit_id'])
        print info
        # info = [request.POST['employee_id'], request.POST['date']]
        return render(request, 'DB_LAB2/Accounting.html', {'emp' : emp, 'emps': emps, 'info': info})
    return render(request, 'DB_LAB2/Accounting.html', {'emp' : emp, 'emps': emps})

def addvisiting(request):
    if request.method == "POST":
        if request.POST["employee_id"] != "" and request.POST["date"] != "":
            db.AddVisiting(request.POST)
        return HttpResponseRedirect('/Accounting')

def deletevisiting(request):
    if request.method == 'POST':
        db.DeleteVisiting(request.POST)
        return HttpResponseRedirect('/Accounting')

def showwithfamily(request):
    if request.method == 'POST':
        emp = db.ShowEmployeeWithFamily(request.POST)
        return render(request, 'DB_LAB2/ShowAllInfo.html', {'emp' : emp})
    else:
        return HttpResponseRedirect('/ShowAllInfo')

def datesearch(request):
    if request.method == 'POST':
        emp = db.DateSearch(request.POST)
        return render(request, 'DB_LAB2/ShowAllInfo.html', {'emp' : emp})
    else:
        return HttpResponseRedirect('/ShowAllInfo')

def exactlysearch(request):
    if request.method == 'POST':
        emp = db.ExactlySearch(request.POST)
        return render(request, 'DB_LAB2/ShowAllInfo.html', {'emp' : emp})
    else:
        return HttpResponseRedirect('/ShowAllInfo')

def booleanmodesearch(request):
    if request.method == 'POST':
        emp = db.BooleanModeSearch(request.POST)
        return render(request, 'DB_LAB2/ShowAllInfo.html', {'emp' : emp})
    else:
        return HttpResponseRedirect('/ShowAllInfo')


def editvisiting(request):
    if request.method == 'POST':
        db.EditVisit(request.POST)
        return HttpResponseRedirect('/Accounting')

def filldb(request):
    if request.method == 'POST':
        db.FillDB()
        return HttpResponseRedirect('/')

def cleardb(request):
    if request.method == 'POST':
        db.ClearDB()
        return HttpResponseRedirect('/')