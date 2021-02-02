# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 04:51:56 2021

@author: VolkanKarakuş
"""

#%% polymorphism (cok bicimlilik)
# employee adinda bir parent classim olsun.
# buna her sene belirli bir zam yapicam.z()  0.1 olsun.

# employee'nin subclass'i computerEng olsun. 
# burada da bir zam methodu olsun. z()  0.2 olsun.

# bir baska subclass electricEng olsun.
# burda da zam methodu z() 0.3 olsun.

class Employee(object):
    def raising(self):
            raise_rate=0.1
            result=100+100*raise_rate
            print('Employee :',result)
    
class compEng(Employee):
    def raising(self):
        raise_rate=0.2
        result=100+100*raise_rate
        print('compEng :',result)
        
class EEE(Employee):
    def raising(self):
        raise_rate=0.3
        result=100+100*raise_rate
        print('EEE :',result)
    
e1=Employee()
ce=compEng()
eee=EEE()

employee_list=[ce,eee]
for employee in employee_list:
    employee.raising()