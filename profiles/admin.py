from django.contrib import admin
from .models import HumanProfile, DogProfile, Breed

class DogProfileInline(admin.TabularInline):
    model = HumanProfile.dogs.through  # This represents the through model of the ManyToManyField
    extra = 1

class HumanProfileAdmin(admin.ModelAdmin):
    inlines = [DogProfileInline]

class DogProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'age', 'bitten', 'rough_play', 'vaccinated']
    list_filter = ['breed', 'age', 'bitten', 'rough_play', 'vaccinated']
    search_fields = ['name']

admin.site.register(HumanProfile, HumanProfileAdmin)
admin.site.register(DogProfile, DogProfileAdmin)
admin.site.register(Breed)