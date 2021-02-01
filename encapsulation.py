# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:06:35 2021

@author: VolkanKarakuş
"""

#%% ENCAPSULATION (kapsulleme)
# method yada variable'lara erisimi kisitlama.

class bankAccount(object):
    def __init__(self,name,money,adress):
        self.name=name          #global attribute
        self.__money=money      #private attribute
        self.adress=adress
        
    #class'larin icinde private'lari modifiye etmek icin get ve set gerekli.
    "global get and global set "
    def getMoney(self):
        return self.__money  # para miktarini ögrenmek istiyorum.
    
    def setMoney(self,amount):
        self.__money=amount
    
    #private method
    def __increase(self):  
        self.__money+=500     # zam 
    
    def getIncrease(self):
        return self.__increase()
        
p1=bankAccount('volkan',20,'mugla')
p2=bankAccount('michael',15,'london')

print('get Method :',p1.getMoney()) # cagirma

p1.setMoney(500) #modify etme
print('set Method :',p1.getMoney()) # modify sonrasi cagirma yine get ile.

# p1.__increase() yaparsam bulamaz cunku private.
# print('after raise :',p1.getMoney())

