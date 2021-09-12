#PROGRM TO CALCULATE ELECRICITY BILL:

name=input("Enter name of the customer :")                              #Taking input for name of customer.

unit=int(input("Enter the meter reading of customer:"))                 #Taking input of meter reading of customer.

print("Name:",name)                                                     #Takimg output for name of customer.

if(unit<=100):                                                          #Taking output for bill using if elif ladder.
    
    rs=unit*3                                                           #Checking conditions if meter reading is less than or equal to 100.
    
    print("Elecricity bill is Rs.:",rs)                                 #Taking output for meter reading less than or equal to 100.
    

elif(unit>100 and unit<=500):                                           #Checking conditions if meter reading is grater than 100 and less than or equal to 500.
    
    rs=unit*7
    
    print("Elecricity bill is Rs.:",rs)                                 #Taking output for meter reading grater than 100 and less than or equal to 500.

elif(unit>500 and unit<=1000):                                          #Checking conditions if meter reading is grater than 500 and less than or equal to 1000.
    
    rs=unit*9
    
    print("Elecricity bill is Rs.:",rs)                                 #Taking output for meter reading grater than 500 and less than or equal to 1000.
    

elif(unit>1000):                                                        #Checking conditions if meter reading is greater than 1000.
    
    rs=unit*11
    
    print("Elecricity bill is Rs.:",rs)                                 #Taking output for meter reading greater than 1000.

else:
    print("Wrong input.")                                               
