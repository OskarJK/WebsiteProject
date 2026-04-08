from django.contrib import admin
from .models import InstagramPost, ManualPost, Recipe
# Register your models here.


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'instagram_url')
    
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

