from django.contrib import admin
from django.utils.html import format_html
from .models import AboutMe, Contact, ContactMessage

# Register your models here.

#Informacje o mnie
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')

#Informacje kontaktowe
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'show_instagramURL', 'show_facebookURL')

    def show_instagramURL(self, obj):
        if obj.link_instagram is not None:
            return format_html(f"<a href='{obj.link_instagram}' target='_blank'>{obj.link_instagram}</a>")
        else:
            return "Brak linku"
        
    def show_facebookURL(self, obj):
        if obj.link_facebook is not None:
            return format_html(f"<a href='{obj.link_facebook}' target='_blank'>{obj.link_facebook}</a>")
        else:
            return "Brak linku"
    
    show_instagramURL.short_description = "Link do Instagrama"
    show_facebookURL.short_description = "Link do Facebooka"

#Formularz kontaktowy
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'created_at')

    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')