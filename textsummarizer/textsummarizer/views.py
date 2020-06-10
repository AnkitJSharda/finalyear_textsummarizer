import requests
from django.shortcuts import render
from subprocess import run, PIPE
import sys

def button(request):
    return render(request,"home.html")

def external(request):
    inp = request.POST.get('param')
    inp1 = request.POST.get('retain')
    out = run([sys.executable,"C://Users//Dell//Desktop//dj1//test.py",inp,inp1],shell=False,stdout=PIPE)
    print(out)
    return render(request,"home.html",{"data1":out.stdout.decode("UTF-8")})
    # return render(request,"home.html",{"data1":out.stdout.decode("UTF-8")})

