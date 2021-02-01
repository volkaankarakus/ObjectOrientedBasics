# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:31:43 2021

@author: VolkanKarakuş
"""

#%% INHERITANCE(MIRAS)
# daha onceden yapilmis bir classin ozelliklerini ya da methodlarini kullanarak yeni bir class yaratmadir.

# Animal class'imda run/walk gibi temel ozellikler olsun.
# alt class'i monkey'de tirmanabilme (climb), bird'de fly olsun.

"parent class"
class Animal(object):
    def __init__(self):
        print('animal is created.')
        
    def toString(self):
        print('animal')
        
    def walk(self):# bu hayvanlarin genel ozelligi, child classa yazmama gerek yok.
        print('animal walk.')

"child classes (Monkey and Bird)"
class Monkey(Animal):
    def __init__(self):
        super().__init__() # burasi parent classin initializer icerigini child classa aktarma.
        print('monkey is created')
        
    def toString(self):
        print('monkey')
        
    
    def climb(self):
        print('monkey can climb.')

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print('bird is created.')
    
    def fly(self):
        print('bird can fly.')
        

    
m1=Monkey() # output=animal is created. monkey is created
m1.toString() #output=monkey
m1.walk() # output=animal walk.
m1.climb() # output=monkey can climb.
print('--------')
b1=Bird()
b1.walk()
b1.fly()

