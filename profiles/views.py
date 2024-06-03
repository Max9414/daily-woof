from django.shortcuts import render
from .forms import BreedForm
from .models import Breed


# Create your views here.

def create_breed(request):
    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            breed = form.cleaned_data['breed']
            new_breed = form.cleaned_data['new_breed']

            if new_breed:
                breed, created = Breed.objects.get_or_create(breed=new_breed)
            form.instance.breed = breed
            form.save()
            return redirect('success')  # Replace with your success URL
    else:
        form = BreedForm()

    return render(request, 'create_breed.html', {'form': form})