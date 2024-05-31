from django.shortcuts import render

# Create your views here.

def petcare(request):
    return render(request, 'petcare/petcare.html')