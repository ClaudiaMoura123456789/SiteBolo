from django.contrib import admin
from .models import Bolo, Item

# Register your models here.

@admin.register(Bolo)
class BoloAdmin(admin.ModelAdmin):
    list_display = ["nome","tipo","sabor"]
    search_fields = ["nome"]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["sabor","cobertura","recheio", "tipodemassa"]
    search_fields = ["recheio"]    



   
