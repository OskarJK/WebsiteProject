from django.contrib import admin
from django.utils.html import format_html
from .models import InstagramPost, ManualPost, Recipe
# Register your models here.


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'show_instagramURL')

    #URL widoczny jako link(klikalny w nowym oknie)
    def show_instagramURL(self, obj):
        if obj.instagram_url is not None:
            return format_html(f"<a href='{obj.instagram_url}' target='_blank'>{obj.instagram_url}</a>")
        else:
            return "Brak linku"
        
    show_instagramURL.short_description = "Link do posta" 
    
@admin.register(ManualPost)
class ManualPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    #Filtrowanie po dacie utworzenia
    list_filter = ('title', 'created_at',)
    search_fields = ('title',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    #Filtrowanie po dacie utworzenia i składnikach
    list_filter = ('created_at', 'ingredients',)
    search_fields = ('title',)

