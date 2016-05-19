from django.shortcuts import render
from .class_db import MyDataDase

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
