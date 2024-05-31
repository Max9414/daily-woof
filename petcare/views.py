from django.shortcuts import render

# Create your views here.

def breeds(request):
    return render(request, 'petcare/petcare.html')