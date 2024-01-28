from django.shortcuts import render

# Create your views here.


def BASE(request):
    return render(request, 'base.html')
def App(request):
    return render(request, 'home.html')
