from django.shortcuts import render, redirect

# Create your views here.

def open_backpack(request):
    return render(request, 'backpack/backpack.html')
