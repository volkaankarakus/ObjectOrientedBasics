# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:23:22 2021

@author: VolkanKarakuş
"""
class Calisan:
    
    zamOrani=1.8
    counter=0 # calisan sayisi icin counter
    def __init__(self,isim,soyisim,maas): # Bu bizim constructor methodumuz
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        
        Calisan.counter+=1 # self'li yapsaydik hep 1 degerini vericekti. self class'i temsil eder, objeyi degil.
    def giveNameSurname(self):
        return self.isim+' '+self.soyisim
    
    def mail(self):
        return self.isim+self.soyisim+'@gmail.com'
    
    
    def maasaZam(self):
        self.maas=self.maas*self.zamOrani
        
calisan1= Calisan('Volkan','Karakus',100)
calisan2=Calisan('Busra','Mulayim',200)
calisan3=Calisan('Merve','Tugce',300)
calisan4=Calisan('Gungor','Uludag',400)


# En yuksek maas alani bul.
liste=[calisan1,calisan2,calisan3,calisan4]
maxValue=calisan1.maas
maxValueName=calisan1.maas
for each in liste:
    if maxValue>each.maas:
        continue
    elif maxValue<each.maas:
        maxValue=each.maas
        maxValueName=each.giveNameSurname()
    else:
        continue
    
print('En yüksek maasi alan kisi :',maxValueName,'ve maası',maxValue)
