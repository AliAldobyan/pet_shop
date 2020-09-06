from django.shortcuts import render, redirect
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

def create_pet(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('pet-list')

    context = {
        "form" : form
    }
    return render(request, 'create_pet.html', context)
