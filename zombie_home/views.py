from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'zombie_home/homepage.html')