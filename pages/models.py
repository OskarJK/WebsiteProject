from django.db import models

# Create your models here.
class AboutMe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię i Nazwisko")
    description = models.TextField(blank=True, null=True, verbose_name="Opis")
    image = models.ImageField(upload_to='about_me_images/', blank=True, null=True, verbose_name="Zdjęcie profilowe")

    class Meta:
        verbose_name = "O mnie"
        verbose_name_plural = "O mnie"

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię i Nazwisko")
    email = models.EmailField(blank=True, null=True, verbose_name="Adres e-mail")
    link_instagram = models.URLField(blank=True, null=True, verbose_name="Link do Instagrama")
    link_facebook = models.URLField(blank=True, null=True, verbose_name="Link do Facebooka")
    
    class Meta:
        verbose_name = "Moje dane kontaktowe"
        verbose_name_plural = "Moje dane kontaktowe"

    def __str__(self):
        return f"{self.name} ({self.email})"
    
MessageStatus = (
    ('New', 'Nowa'),
    ('Read', 'Przeczytana'),
    ('Finished', 'Zakończona'),
)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię")
    email = models.EmailField(verbose_name="Adres e-mail")
    subject = models.CharField(max_length=200, verbose_name="Temat")
    message = models.TextField(verbose_name="Treść wiadomości")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    status = models.CharField(choices=MessageStatus, default='New', max_length=20, verbose_name="Status wiadomości")

    class Meta:
        verbose_name = "Wiadomość od klientów"
        verbose_name_plural = "Wiadomości od klientów"


    def __str__(self):
        return f"Wiadomość od {self.name} ({self.email})"