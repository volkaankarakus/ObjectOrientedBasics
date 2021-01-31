# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:44:43 2021

@author: VolkanKarakuş
"""
#%% CLASS

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
        
# isci1=Calisan('Volkan','Karakus',100)

# print(isci1.giveNameSurname())
# print(isci1.mail())

calisan1= Calisan('Volkan','Karakus',100)
print('İlk maas :',calisan1.maas)
calisan1.maasaZam()
print('Calisana zam yapildi.Yeni maas :',calisan1.maas)
