from django.contrib import admin
from api.models import Country,State

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display=('Country_id','name')
    search_fields=('name',)

class StateAdmin(admin.ModelAdmin):
    list_display=('name','Country')
    list_filter=('Country',)


admin.site.register(Country,CountryAdmin)
admin.site.register(State,StateAdmin)

# from django.contrib import admin
# from .models import Country, State

# admin.site.register(Country)
# admin.site.register(State)
