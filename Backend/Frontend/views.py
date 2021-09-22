from django.shortcuts import render

# Create your views here.

def OpeningSite(request):
    return render(request, 'index.html')

def Action(request):
    return render(request, 'akcja.html')

def Horror(request):
    return render(request, 'horror.html')

def Comedy(request):
    return render(request, 'komedia.html')

def Animation(request):
    return render(request, 'animacja.html')