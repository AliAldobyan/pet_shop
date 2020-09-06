from django.shortcuts import render
from .models import Pet
# Create your views here.

def list_view(request):
    pets = Pet.objects.all()
    context ={
        # should be :
        'pets': pets
    }
    return render(request, 'list.html', context)

def detail_view(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    context ={
        # should be :
        'pet': pet
    }
    return render(request, 'detail.html', context)
