from django import forms
from .models import SportovniAkce

# ukol:
# jak jste se o nás dozvěděli

class RodicForm (forms.Form):
    rodic_jmeno = forms.CharField(max_length=30, label= "Jméno rodiče", widget=forms.TextInput(attrs={"class":"form-widget input-parent-name", "placeholder": "Jméno"}))
    rodic_prijmeni = forms.CharField(max_length=30, label= "Přijmení rodiče", widget=forms.TextInput(attrs={"class":"form-widget input-parent-surname", "placeholder":"Přijmení"}))
    bydliste = forms.CharField(max_length=100, label="Bydliště", widget=forms.TextInput(attrs={"class":"form-widget input-adress", "placeholder":"Bydliště"}))
    email = forms.EmailField(label= "Email", widget=forms.TextInput(attrs={"class":"form-widget input-email","placeholder":"@"}))
    telefon = forms.CharField(max_length=31, label= "Telefon", widget=forms.TextInput(attrs={"class":"form-widget input-phone", "placeholder":"Telefon"}))
    

class DiteForm (forms.Form):
    dite_jmeno = forms.CharField(max_length=30, label= "Jméno dítěte",widget=forms.TextInput(attrs={"class":"form-widget input-child-name", "placeholder":"jméno"}))
    dite_prijmeni = forms.CharField(max_length=30,label= "Příjmení dítěte",widget=forms.TextInput(attrs={"class":"form-widget input-child-surname", "placeholder":"Příjmení"}))
    vek = forms.IntegerField(label= "Věk", widget=forms.TextInput(attrs={"class":"form-widget input-child-year", "placeholder": "věk"})) 
    alergie = forms.CharField(max_length=130, label= "Alergie",required=False, widget=forms.Textarea(attrs={"class":"form-widget_alergie"}))
    poznamka = forms.CharField(max_length=300, label="Poznámka", required=False, widget=forms.Textarea(attrs={"class":"form-widget_poznamka"}))
    #cizí klíč akce one to many vazba ModelMultipleChoiceField vazba many to many
    akce = forms.ModelChoiceField(queryset=SportovniAkce.objects.all(),label="Vyberte sportovní akci", widget=forms.Select)

    


    
    
    