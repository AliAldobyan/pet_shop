from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
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
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form" : form
    }
    return render(request, 'create_pet.html', context)

def update_pet(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet_obj)
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid():
            form.save()
            return redirect(pet_obj)
    context = {
        "form" : form,
        "pet": pet_obj,
    }
    return render(request, 'update_pet.html', context)

def delete_pet(request, pet_id):
    Pet.objects.get(id=pet_id).delete()
    return redirect('pet-list')
