# ukoly: 
# nastavit ordering deti podle veku, ale nejdřív asi vyřešit datum narozeni
# pořádání akce od kdy do kdy , upravit 
 
from django.db import models
from phone_field import PhoneField
# Create your models here.

class Rodic (models.Model):
    rodic_jmeno = models.CharField(max_length=30)
    rodic_prijmeni = models.CharField(max_length=30)
    bydliste = models.CharField(max_length=80)
    email = models.EmailField()
    telefon = PhoneField(max_length=31)
    
    def __str__(self):
        # důležité pro výpis ve formulaři na klientovi!! 
        return f"{self.rodic_jmeno} {self.rodic_prijmeni}"

    class Meta:
        verbose_name_plural = "Rodiče"

# null=True: Tento argument říká databázi, že pole může mít hodnotu NULL, což znamená, že 
            # v databázi může být prázdné (bez hodnoty). není potřba u vazby many to many 
#blank=True: Tento argument říká formuláři, že pole je volitelné a může být 
            #prázdné při validaci formuláře. To znamená, že pole není povinné. V adminu pak mohu vytvářest 
            # sportovní akce bez dětí.
        
class Dite (models.Model):
    dite_jmeno = models.CharField(max_length=30)
    dite_prijmeni = models.CharField(max_length=30)
    vek = models.IntegerField(null=True) 
    alergie = models.CharField(max_length=80, blank=True)
    poznamka = models.CharField(max_length=200, null=True, blank=True)
    rodic = models.OneToOneField(Rodic, on_delete=models.CASCADE,null=True)
    akce = models.ForeignKey("SportovniAkce", on_delete=models.CASCADE, null=True)
     
    def __str__(self):
        # důležité pro výpis ve formulaři na klientovi!! 
        return f"{self.dite_jmeno} { self.dite_prijmeni}"

    class Meta:
        verbose_name_plural = "Děti"

class SportovniAkce(models.Model):
    nazev = models.CharField(max_length=100)
    termin_od = models.DateField(null=True)
    termin_do = models.DateField(null=True)
    seznam_deti = models.ManyToManyField(Dite, blank=True)

    def __str__(self):
        # důležité pro výpis ve formulaři na klientovi + Admin!! 
        return (f"{self.nazev} datum: {self.termin_od} {self.termin_do}")
   
    class Meta:
        verbose_name_plural = "Sportovní Akce"
