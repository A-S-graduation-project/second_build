from django.shortcuts import render

# Create your views here.
def board (request):
    return render(request, 'board.html')

def boarddetail (request):
    return render(request, 'boarddetail.html')