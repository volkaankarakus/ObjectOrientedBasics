# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:27:57 2021

@author: VolkanKarakuş
"""

#%% abstract class (soyut class)
#suana kadar parent(super) ve child(sub) classlar gorduk.
#abstract classlar, sub classlar icin sablon gorevi gorurler ve kullanılacak ortak fonksiyonlari kendi icinde tutar.

from abc import ABC,abstractmethod

# "superclass"
# class Animal(object): 
#     pass

class Animal(ABC):
#1. KURAL : animal ile ilgili hicbir obje yaratamam.
    @abstractmethod()
    def walk(self):
        pass
    
    @abstractmethod() # run, abstract olmasaydi da Animal abstract sayilicakti.
    def run(self):
        pass
    
#2.KURAL: abstractte kullanilan method, child classta kullanilmak zorundadir.

"subclass"
class Bird(Animal):
    def __init__(self):
        print('bird')
        
    def walk(self):
        print('walk')
        
    def run(self):
        print('run')