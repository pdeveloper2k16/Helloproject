from django.shortcuts import render
from django.http import HttpResponse
from secondapp.models import Employee

def employee_info_views(request):
    employees = Employee.objects.all()
    data = {'employees':employees}
    res = render(request, 'secondapp/employee.html',data)
    return res

def showTest(request):
    que = "Who developed C language ?"
    a = "Ken Thomson"
    b = "Denise Ritche"
    c = "Bajarane"
    d = "Pradeep"
    level = "Easy"
    data = {'que': que, 'a': a, 'b': b, 'c': c, 'd': d,'level': level}

    res = render(request, 'secondapp/test.html', context=data)
    return res
def result(request):
    temp = "<h1>Welcome to Second app</h1>"
    temp += "<p>Welcome to result</p>"
    return HttpResponse(temp)
