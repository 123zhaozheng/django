from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request,name):
    value = 'This is test!'
    print(name)
    # return render(request, "index.html")
    return HttpResponseRedirect('This is test!')
def userLogin(request):
    return HttpResponse('This is test!')