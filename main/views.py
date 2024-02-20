from django.shortcuts import render, get_object_or_404, redirect
from .models import Destinacija, Smjestaj, Rezervacija, DodatniDetalji, SmjestajRezervacija
from .forms import RezervacijaForm


def homepage(request):
    destinacije = Destinacija.objects.all()
    smjestaji = Smjestaj.objects.all()
    rezervacije = Rezervacija.objects.all()
    
    context = {
        'destinacije': destinacije,
        'smjestaji': smjestaji,
        'rezervacije': rezervacije,
    }
    
    return render(request, 'homepage.html', context)


def update_rezervacija(request, rezervacija_id):
    rezervacija = get_object_or_404(Rezervacija, pk=rezervacija_id)
    
    if request.method == 'POST':
        form = RezervacijaForm(request.POST, instance=rezervacija)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RezervacijaForm(instance=rezervacija)

    return render(request, 'update_rezervacija.html', {'form': form})

def delete_rezervacija(request, rezervacija_id):
    rezervacija = get_object_or_404(Rezervacija, pk=rezervacija_id)
    
    if request.method == 'POST':
        rezervacija.delete()
        return redirect('homepage')
    
    return render(request, 'delete_rezervacija.html', {'rezervacija': rezervacija})


def add_rezervacija(request):
    if request.method == 'POST':
        form = RezervacijaForm(request.POST)
        if form.is_valid():
            rezervacija = form.save()
            return redirect('homepage')
    else:
        form = RezervacijaForm()

    return render(request, 'add_rezervacija.html', {'form': form})

