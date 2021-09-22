from django.shortcuts import render

# Create your views here.

def OpeningSite(request):
    return render(request, 'index.html')