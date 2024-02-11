from django.shortcuts import render

def open_backpack(request):
    return render(request, 'backpack/backpack.html')
