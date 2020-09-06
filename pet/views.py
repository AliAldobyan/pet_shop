from django.shortcuts import render
from .models import Pet
# Create your views here.

def list_view(request):
    pets = Pet.objects.all()
    context ={
        'pets' = pets
    }
    return render(request, 'list.html', context)
