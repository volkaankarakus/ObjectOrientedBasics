# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 00:27:35 2021

@author: VolkanKarakuş
"""
from rent import carRent,bikeRent,Costumer

bike = bikeRent(100) # icine stock alir.
car=carRent(10)
costumer=Costumer()
mainMenu=True

while True:
    if mainMenu:
        print("""
              ************* VEHICLE RENTAL SHOP *************
              A. Bike Menu
              B. Car Menu
              Q. Exit 
              """)
        mainMenu=False # herhangi bir tusa basilinca
        
        choice =input('Enter choice :')
        
        if choice =='a' or 'A':
            print("""
                  ************* BIKE MENU *************
                  1. Display available bikes
                  2. Request a bike on hourly basis $5
                  3. Request a bike on daily basis $84
                  4. Return a bike 
                  5. Main Menu
                  6. Exit
                  """
                  )
              
            choice=input('Enter choise :')
            try :
                choice=int(choice)
            except ValueError:
                print('Value must be integer.')
                continue
            
            if choice ==1:
                bike.displayStock()
                choice='A'
            
            elif choice==2:
                costumer.rentalTimeBike=bike.rentHourly(costumer.requestVehicle('bike'))
                costumer.rentalBasisBike=1 # saatlik
                mainMenu=True
                print('----------')
                
            elif choice==3:
                costumer.rentalTimeBike=bike.rentDaily(costumer.requestVehicle('bike'))
                costumer.rentalBasisBike=2 #gunluk
                mainMenu=True
                print('----------')
                
            elif choice==4:
                costumer.bill=bike.returnVehicle(costumer.returnVehicle('bike'),'bike')
                costumer.rentalBasisBike,costumer.rentalTimeBike,costumer.bikes=0,0,0
                mainMenu=True
                
            elif choice==5:
                mainMenu=True
                
            elif choice ==6:
                break
            
            else :
                print('Invalid input. Please enter a number between 1-6.')
                mainMenu=True
                
        elif choice =='B' or 'b':
            
            print("""
                  ************* BIKE MENU *************
                  1. Display available cars
                  2. Request a car on hourly basis $10
                  3. Request a car on daily basis $192
                  4. Return a car 
                  5. Main Menu
                  6. Exit
                  """
                  )
            
            choice=input('Enter choise :')
            try :
                choice=int(choice)
            except ValueError:
                print('Value must be integer.')
                continue
        
            if choice ==1:
                bike.displayStock()
                choice='B'
                
            elif choice==2:
                costumer.rentalTimeBike=bike.rentHourly(costumer.requestVehicle('bike'))
                costumer.rentalBasisBike=1 # saatlik
                mainMenu=True
                print('----------')
                    
            elif choice==3:
                
                costumer.rentalTimeBike=bike.rentDaily(costumer.requestVehicle('bike'))
                costumer.rentalBasisBike=2 #gunluk
                mainMenu=True
                print('----------')
                    
            elif choice==4:
                costumer.bill=bike.returnVehicle(costumer.returnVehicle('bike'),'bike')
                costumer.rentalBasisBike,costumer.rentalTimeBike,costumer.bikes=0,0,0
                mainMenu=True
                    
            elif choice==5:
                mainMenu=True
                    
            elif choice ==6:
                break
                
            else :
                print('Invalid input. Please enter a number between 1-6.')
                mainMenu=True
            
        elif choice =='Q' or 'q':
            
            break
        
        else:
            print('Invalid input. Please enter A-B-Q')
            
        print('Thank you for using the vehicle rental shop.')
            
            
            
            
                
        