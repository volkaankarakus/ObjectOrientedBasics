# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 01:07:38 2021

@author: VolkanKarakuş
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:13:16 2021

@author: VolkanKarakuş
"""

#%% 
# vehicleRent(parent Class)
#   displayStock() 
#   rentHourly()
#   rentDaily()
#   returnVehicle()

# carRent and bikeRent() (child Classes)
#   discount()

# Costumer Class (yukaridakileri kapsar)
#   requestVehicle()
#   returnVehicle()

#%%
import datetime

"parent class"
class vehicleRent(object):
    def __init__(self,stock): # arac sayisini stockta tut.
        self.stock=stock
        self.now=0 # bill'de odeme yaparken ne kadar kiralandigina gore 
    
    def displayStock(self):
        "display stock"
        print('{} vehicle available to rent'.format(self.stock))
        
        return self.stock
    
    def rentHourly(self,n): # n=saatlik kiralanmak istenen arac sayisi
        "rent hourly"
        if n<=0:
            print('Number should be positive.')
            
            return None #hicbir arac kiralanmadi.
        
        elif n>self.stock:
            print('Sorry, {} available to rent'.format(self.stock))
            
            return None
        
        else :
            self.now=datetime.datetime.now()
            print('Rented a {} vehicle for hourly at {} hours.'.format(n,self.now().hour))
            self.stock-=n # stockta bulunan araci guncelle.
            
            return self.now # musteri araci geri getirdiginde saate bakicam. farka gore ucret donucek.
            
    
    def rentDaily(self,n):
        "rent daily"
        if n<=0:
            print('Number should be positive.')
            
            return None 
        
        elif n>self.stock:
            print('Sorry, {} available to rent'.format(self.stock))
            
            return None
        
        else :
            self.now=datetime.datetime.now()
            print('Rented a {} vehicle for daily at {} hours.'.format(n,self.now().hour))
            self.stock-=n 
            
            return self.now 
    
    def returnVehicle(self,request,brand):
        "return a bill"
        carHourlyPrice=10
        carDailyPrice=carHourlyPrice*0.8*24
        bikeHourlyPrice=6
        bikeHourlyPrice=bikeHourlyPrice*0.7*24
        
        rentalTime,rentalBasis,numberOfVehicle=request # sure, saatlik-gunluk,kiralanan arac
        bill=0
        
        if brand=='car':
            if rentalTime and rentalBasis and numberOfVehicle: # bu uc deger de girildiyse
                self.stock+=numberOfVehicle # arac iadesini stock'a ekleyerek stock guncellemesi.
                now=datetime.datetime.now() # bu now, local parametre. self.now degil.
                rentalPeriod= rentalTime-now # kac saat kiralandi.
                
                if rentalBasis==1: # hourly
                    bill=rentalPeriod.seconds()/3600*carHourlyPrice*numberOfVehicle
                    
                elif rentalBasis==2: # daily
                    bill=rentalPeriod.seconds()/3600**24*carDailyPrice*numberOfVehicle
                    
                if (2<=numberOfVehicle):
                    print('You have 20% discount')
                    bill=bill*0.8
                    
                print('Thank you for returning you car.')
                print('Price : ${} '.format(bill))
                
                return bill
                
        elif brand=='bike':
            if rentalTime and rentalBasis and numberOfVehicle: # bu uc deger de girildiyse
                self.stock+=numberOfVehicle # arac iadesini stock'a ekleyerek stock guncellemesi.
                now=datetime.datetime.now() # bu now, local parametre. self.now degil.
                rentalPeriod= rentalTime-now # kac saat kiralandi.
                
                if rentalBasis==1: # hourly
                    bill=rentalPeriod.seconds()/3600*bikeHourlyPrice*numberOfVehicle
                    
                elif rentalBasis==2: # daily
                    bill=rentalPeriod.seconds()/3600**24*bikeHourlyPrice*numberOfVehicle
                    
                if (4<=numberOfVehicle):
                    print('You have 20% discount')
                    bill=bill*0.8
                    
                print('Thank you for returning you bike.')
                print('Price : ${} '.format(bill))
                
                return bill
            
        else :
             print('You do not rent a vehicle.')
             
             return None
             
"child class 1"
class carRent(vehicleRent):
    
    global discountRate # tum araclar icin discount (global)
    discountRate=15
    
    def __init__(self,stock):
        super().__init__(stock)
    
    def discount(self,b):
        bill =b-(b*discountRate/100)
        return bill
    
"child class 2"
class bikeRent(vehicleRent):
    def __init__(self,stock):
        super().__init__(stock)
        
"costumer"
class Costumer():
    def __init__(self):
        self.bikes=0
        self.rentalBasisBike=0 # bisiklet icin gunluk mu saatlik mi
        self.rentalTimeBike=0 # ne zaman kiralandigi
        
        self.cars=0
        self.rentalBasisCar=0 
        self.rentalTimeCar=0
    
    def requestVehicle(self,brand):
        "take a request bike or car from costumer"
        if brand=='bike':
            bikes=input('How many bikes would you like to rent ?')
            try:
                bikes=int(bikes)
            except ValueError:
                print('Value should be number.')
                return -1 
            
            if bikes<1:
                print('Number of bikes should be greater than zero.')
                return -1
            
            else :
                self.bikes=bikes
                
            return self.bikes
                
            
            
        elif brand=='car':
            cars=input('How many cars would you like to rent ?')
            try:
                cars=int(cars)
            except ValueError:
                print('Value should be number.')
                return -1 
            
            if cars<1:
                print('Number of cars should be greater than zero.')
                return -1
            
            else :
                self.cars=cars
                
            return self.cars
            
            
        else:
            print('Request vehicle error')
            
            return None
    
    def returnVehicle(self,brand):
        "return bikes or cars"
        
        if brand=='bike':
            if self.rentalTimeBike and self.rentalBasisBike and self.bikes:
                
                return self.rentalTimeBike, self.rentalBasisBike,self.bikes
            
            else:
                return 0,0,0
                
        elif brand=='car':
            if self.rentalTimeCar and self.rentalBasisCar and self.car:
                
                return self.rentalTimeCar, self.rentalBasisCar,self.car
            
            else:
                return 0,0,0    
            
        else:
            print('Return vehicle error.') 
