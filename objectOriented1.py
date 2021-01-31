# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:29:31 2021

@author: VolkanKarakuş
"""

#%% methods vs functions

class Employee(object):
    age=25
    salary=1000 # $
    
    #method
    def ageSalaryRatio(self):
        a=self.age/self.salary
        print('Method : age/salary is',a)

employee1=Employee()
employee1.ageSalaryRatio()     

##################################################################   
#function
def ageSalaryRatio(age,salary):
    a=age/salary
    print('Function : age/salary is ',a)
    return a
    
#method, self parametresine sahip.
#   self,class dependenttir.
#function, classla alakasi yok. object ya da self'e bakmaz.
ageSalaryRatio(30,3000)

def findArea(r,pi=3.14):
    area=pi*r**2
    #print(area)
    return area

result1=findArea(10)
result2=findArea(12)
result=result1+result2
print(result)

# %% initializer or constructor

class Animal(object):
    name='dog'
    age=2
    
    def getAge(self):
        return self.age
a1=Animal()
a1Age=a1.getAge()
print('animal age :',a1Age)
#baska bir hayvan girmek istersem yukariyi tekrar tekrar degistirip yazmakla ugrasmam.
#bunun icin initializer(constructor) kullanilirim.

#%%INITIALIZER

class Animal(object):
    def __init__(self,name,age): # selften sonra input parametreleri alirim.
        self.name=name
        self.age=age   
        
    def getAge(self):
        return self.age
        
    def getName(self):
        return print(self.name)
    
a1=Animal('dog',2)
a2=Animal('cat',3)
a3=Animal('bird',5)









