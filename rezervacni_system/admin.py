from django.contrib import admin
from .models import Rodic, Dite, SportovniAkce 

# Register your models here.

class RodicAdmin(admin.ModelAdmin):
    list_display= ("rodic_jmeno","rodic_prijmeni","bydliste","email","telefon")

class DiteAdmin(admin.ModelAdmin):
    list_display= ("dite_jmeno","dite_prijmeni","vek","alergie","poznamka","akce","rodic")
    
class SportovniAkceAdmin(admin.ModelAdmin):
    list_display = ("nazev", "termin_od", "termin_do")
    filter_horizontal = ["seznam_deti"]
    
admin.site.register(Rodic,RodicAdmin)
admin.site.register(Dite,DiteAdmin)
admin.site.register(SportovniAkce, SportovniAkceAdmin)





