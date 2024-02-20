from django.db import models
from django.contrib.auth.models import User

class Destinacija(models.Model):
    ime = models.CharField(max_length=100)
    opis = models.TextField()

    def __str__(self):
        return self.ime

class Smjestaj(models.Model):
    naziv = models.CharField(max_length=100)
    adresa = models.CharField(max_length=255)
    destinacija = models.ForeignKey(Destinacija, on_delete=models.CASCADE)
    kapacitet = models.PositiveIntegerField()
    cena_nocenja = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.naziv

class Rezervacija(models.Model):
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    smjestaj = models.ForeignKey(Smjestaj, on_delete=models.CASCADE)
    datum_dolaska = models.DateField()
    datum_odlaska = models.DateField()
    broj_gostiju = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.korisnik.username} - {self.smjestaj.naziv} - {self.datum_dolaska} do {self.datum_odlaska}"

class DodatniDetalji(models.Model):
    rezervacija = models.OneToOneField(Rezervacija, on_delete=models.CASCADE)
    neki_detalji = models.TextField()

class SmjestajRezervacija(models.Model):
    rezervacija = models.ForeignKey(Rezervacija, on_delete=models.CASCADE)
    smjestaji = models.ManyToManyField(Smjestaj)
