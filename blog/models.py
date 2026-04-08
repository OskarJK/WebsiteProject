from django.db import models

# Create your models here.
class InstagramPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(blank=True, null=True, verbose_name="Opis")
    image = models.ImageField(upload_to='instagram_images/', blank=True, null=True, verbose_name="Zdjęcie")
    instagram_url = models.URLField(blank=True, null=True, help_text="Wklej tutaj link do posta na IG")

    def __str__(self):
        return self.title
    
class ManualPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(blank=True, null=True, verbose_name="Opis")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name="Zdjęcie")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")

    def __str__(self):
        return self.title

class Recipe(models.Model):
    #Główne informacje
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(blank=True, null=True, verbose_name="Opis")
    ingredients = models.TextField(blank=True, null=True, verbose_name="Składniki")
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True, verbose_name="Zdjęcie")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    optional_information = models.TextField(blank=True, null=True, verbose_name="Dodatkowe informacje")
    #Wartości odżywcze
    wartosc_energetyczna = models.CharField(max_length=30, blank=True, null=True, verbose_name="Wartość energetyczna (kcal)")
    bialko = models.CharField(max_length=300, blank=True, null=True, verbose_name="Białko (g)")
    weglowodany = models.CharField(max_length=30, blank=True, null=True, verbose_name="Węglowodany (g)")
    sol = models.CharField(max_length=30, blank=True, null=True, verbose_name="Sól (g)")
    blonnik = models.CharField(max_length=30, blank=True, null=True, verbose_name="Błonnik (g)")
    index_glikemiczny = models.CharField(max_length=30, blank=True, null=True, verbose_name="Indeks glikemiczny")
    ladunek_glikemiczny = models.CharField(max_length=30, blank=True, null=True, verbose_name="Ładunek glikemiczny")
    zelazo = models.CharField(max_length=30, blank=True, null=True, verbose_name="Żelazo (mg)")
    wapn = models.CharField(max_length=30, blank=True, null=True, verbose_name="Wapń (mg)")

    def __str__(self):
        return self.title
    