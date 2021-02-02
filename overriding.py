# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 04:31:54 2021

@author: VolkanKarakuş
"""

class Animal():
    def toString(self):
        print('animal')
        
class Monkey(Animal):
    def toString(self):
        print('monkey')
        
a1=Animal()
a1.toString

m1=Monkey()
m1.toString() #monkey calls overriding method


        