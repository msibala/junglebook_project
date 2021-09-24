from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, 'jungle_app/home_page.html')

def land(request):
    return render(request, 'jungle_app/land.html')

def ocean(request):
    return render (request, 'jungle_app/ocean.html')  

def wing(request):
    return render (request, 'jungle_app/wing.html')  

