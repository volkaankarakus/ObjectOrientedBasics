# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 05:27:08 2021

@author: VolkanKarakuş
"""

# abstract bir shaper class'i kur.
# area,perimeter, toString alsin.
# area ve perimeter abstractmethod olsun, toStringte overriding ve polymorphism olsun.

#subclass'lar square ve circle.

from abc import ABC, abstractmethod
class Shaper(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def toString(self):
        pass
    
"subclasses"
class Square(Shaper):
    def __init__(self,edge):
        self.__edge = edge #encapsulation (disaridan erisimi olmasin.) 
        
    def area(self):
        result =self.__edge**2
        print('Square Area :',result)
        
    def perimeter(self):
        result=self.__edge*4
        print('Square Perimeter :',result)
    
    #overriding and polymorphism
    def toString(self): 
        print('Square Edge :',self.__edge) # pass demedigimiz icin zaten polymorphism yapmis oluyoruz.
        
class Circle(Shaper):
    
    PI=3.14 # constant variable'lar buyuk harfle yazilir.
    
    def __init__(self,radius):
        self.__radius = radius
        
    def area(self):
        result=self.PI*self.__radius**2
        print('Circle Area :',result)
        
    def perimeter(self):
        result=2*self.PI*self.__radius
        print('Circle Perimeter :',result)
            
    def toString(self):
        print('Circle Radius :',self.__radius)
        
        
c=Circle(5)
c.area()
c.perimeter()
c.toString()

s=Square(5)
s.area()
s.perimeter()
s.toString()

        