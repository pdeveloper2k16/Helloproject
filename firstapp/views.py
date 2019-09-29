from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    temp = "<h1>Hello and Welcome to first Django Project<h1>"
    return HttpResponse(temp)
def showContact(request):
    temp = "<h1>Contact Page</h1>"
    temp += "<p>Welcome site : studyzone24.com</p>"
    temp += "<p>Mobile : 9009000200</p>"
    temp += "<p>Email : kpradeep.sdr@gmail.com</p>"
    return HttpResponse(temp)
def about(request):
    msg = "this is an about page"
    return render(request,'firstapp/about.html', {'msg':msg})