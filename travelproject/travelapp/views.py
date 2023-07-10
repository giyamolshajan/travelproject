from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return render(request,"index.html")

#def addition(request):
   # x=request.GET['num1']
   # y=request.GET['num2']
   # result=x+y
   # return render(request,"about.html",{'result':result})


