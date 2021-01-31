# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:49:38 2021

@author: VolkanKarakuş
"""
#calculator project
#%% 

class Calc(object):
    "calculator"
    def __init__(self,value1,value2):
        "initialize values"
        
        #attribute
        self.value1=value1
        self.value2=value2
        
    def Add(self):
        "addition"
        
        return self.value1+self.value2
    
    def Multiply(self):
        "multipication"
        
        return self.value1*self.value2
    
    def Division(self):
        "division"
        
        return self.value1/self.value2
    
    def Subtraction(self):
        "subtraction"
        
        return self.value1-self.value2
while True:
    operation=int(input('Choose the operation: \n1 Add \n2 Multiply \n3 Division \n4 Subtraction'))
    v1=int(input('Enter the value1'))
    v2=int(input('Enter the value2'))
    c1=Calc(v1,v2)
    
    
    
    if operation==1:
        addValue=c1.Add()
        print('Selection is addition \nResult is {}'.format(addValue))
        
    elif operation==2:
        multValue=c1.Multiply()
        print('Selection is multipication \nResult is {}'.format(multValue))
        
    elif operation==3:
        divValue=c1.Division()
        print('Selection is division \nResult is {}'.format(divValue))
        
    elif operation==4:
        subValue=c1.Subtraction()
        print('Selection is subtraction \nResult is {}'.format(subValue))
    else:
        print('Enter one of the given values')
           