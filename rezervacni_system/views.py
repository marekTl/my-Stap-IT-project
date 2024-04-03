# úkoly:
# odhlásit dítě
# platba za akci + výpočet 
# stornovat platbu


from django.shortcuts import render
from .forms import  DiteForm, RodicForm
from .models import Rodic, Dite
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def uvod(request):
    return render(request,"rezervacni_system/uvod.html")

def prihlasit_se(request):
    if request.method == 'POST':
        rodic_form = RodicForm(request.POST)
        dite_form = DiteForm(request.POST)
        
        if rodic_form.is_valid() and dite_form.is_valid():
            rodic = Rodic(
                rodic_jmeno = rodic_form.cleaned_data["rodic_jmeno"],
                rodic_prijmeni = rodic_form.cleaned_data["rodic_prijmeni"],
                bydliste = rodic_form.cleaned_data["bydliste"],
                email = rodic_form.cleaned_data["email"],
                telefon = rodic_form.cleaned_data["telefon"],
            )
            rodic.save()
            
            dite = Dite(
                dite_jmeno = dite_form.cleaned_data["dite_jmeno"],
                dite_prijmeni = dite_form.cleaned_data["dite_prijmeni"],
                vek = dite_form.cleaned_data["vek"],
                alergie = dite_form.cleaned_data["alergie"],
                poznamka = dite_form.cleaned_data["poznamka"],
                akce = dite_form.cleaned_data["akce"],
                rodic = rodic # Přiřazení rodiče k dítěti (Tímto způsobem instanci rodiče přiřadíte k dítěti )
           
            )
            dite.save()
            akce = dite_form.cleaned_data["akce"]
            akce.seznam_deti.add(dite)
           
            
            return HttpResponseRedirect(reverse("uspesna_registrace")) # funkce reverse vytvoření url adresy 
    else:
        rodic_form = RodicForm()
        dite_form = DiteForm()
        
    return render(request, "rezervacni_system/prihlaska.html", {
        "rodic_form": rodic_form,
        "dite_form": dite_form,
    })
def uspesna_registrace(request):
    return render(request,"rezervacni_system/uspesna_registrace.html")





    
 