#i would like to be able to go back and forth between the two temperatures. 

'''
We're going to change Celcius to Farenheit 
How to change Celcius To Fareneheit: Divide by 5, multiply by 9, add 32
Have C*
    ask user for tempurature they want to concert to celcius in celcius
    We will prompt user to enter tempurature in celcius
    -store initual tempurature-
Calculate temp in F from user given temp in C
    how: Divide by 5, multiply by 9, add 32
Tell user temp in Farenheit

'''

# user input
userTempInC=input("What is the temperature in Celcius that you would like to convert? ")
#print(userTempInC)

# calc
tempInFStep1=float(userTempInC)/5
tempInFStep2=float(tempInFStep1)*9
tempInF=float(tempInFStep2)+32

# output
print( )
print("=============================<3=============================")
print("The Tempurature Is:",tempInF)
