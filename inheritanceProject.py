# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:57:52 2021

@author: VolkanKarakuş
"""

"parent class"
class Website(object):
    def __init__(self,name,surname):
        self.name = name
        self.surname=surname
        
    def loginInfo(self):
            print(self.name+' '+self.surname)


"child classes"
class Website1(Website):
    def __init__(self,name,surname,ID): # parent class initinde bunlar oldugu icin buraya da almak zorundayim.
                                        # websitesine giris sekli ID ile.
        Website.__init__(self,name,surname) #bunu daha once super ile yapmistik.
        self.ID=ID
        
    def login(self):
        print(self.name+' '+self.surname+' '+self.ID) # website1 icin giris bilgileri name,surname ve ID.


class Website2(Website):
    def __init__(self,name,surname,email): 
        Website.__init__(self,name,surname)
        self.email=email
        
    def login(self):
        print(self.name+' '+self.surname+' '+self.email) 

person1=Website('volkan','karakus')
person2=Website1('volkan','karakus','123')
person3=Website2('volkan','karakus','@gmail')

print(person3.email)
print(person3.login())
print(person3.loginInfo())