from django.shortcuts import render

# Create your views here.

def Login (request):
    return render(request, 'testlogin.html')

def Mypage (request):
    return render(request, 'mypage.html')