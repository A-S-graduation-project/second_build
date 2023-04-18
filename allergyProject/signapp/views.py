from django.shortcuts import render

# Create your views here.

def Login (request):
    return render(request, 'login.html')

def Signup (request):
    return render(request, 'signup.html')

def Mypage (request):
    return render(request, 'mypage.html')