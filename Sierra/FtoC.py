#i would like to be able to go back and forth between the two temperatures. 
'''
We're going to change Farenheit to Celcius
How to change fahrenheit to celcius: multiply f by 1.8 (or 9/5) and add 32.

Have F*
    ask user for tempurature they want to concert to celcius in farenheit
    We will prompt user to enter tempurature in farenheit
    -store initual tempurature-
Calculate temp in C from user given temp in F
    how: Deduct 32, then multiply by 5, then divide by 9.
Tell user temp in Celcius 

'''

# user input
userTempInF=input("What is the temperature in Farenheit that you would like to convert? ")
#print(userTempInC)

# calc nice job sierra 
tempInCelStep1=float(userTempInF)-32
tempInCelStep2=float(tempInCelStep1)*5
tempInCel=float(tempInCelStep2)/9

# output
print( )
print("=============================<3=============================")
print("The Tempurature Is:",tempInCel)





