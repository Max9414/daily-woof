from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Breed

# Create your views here.

class BreedsList(generic.ListView):
    model = Breed
    template_name = "breeds/breeds.html"
    context_object_name = 'breeds'
    paginate_by = 4

def breed_detail(request, id):
    """
    Display an individual :model:`breeds.Breed`.

    **Context**

    ``breed``
        An instance of :model:`breeds.Breed`.

    **Template:**

    :template:`breeds/breed_detail.html`
    """

    model = Breed
    breed = get_object_or_404(model, pk=id)
    return render(
        request, 'breeds/breed_detail.html', {'breed': breed}
    )
    

# easy view to check if html is correctly linked and functioning
# def breeds(request):
#     return render(request, 'breeds/breeds.html')