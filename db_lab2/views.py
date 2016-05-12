from django.shortcuts import render
from .class_db import MyDataDase

db = MyDataDase()

def all_posts(request):
    emp = db.AllEmployees()
    return render(request, 'DB_LAB2/all_posts.html', {'emp': emp})

#def click(request):
#    emp = db.Test()
#    return render(request, 'DB_LAB2/all_posts.html', {'emp': emp})
