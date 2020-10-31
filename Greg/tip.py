'''

~this is a multi-line comment. Everything between three ' is a multiline
Its common to have a multiline comment at the top of your project to keep track of notes and what youre doing.
#this is a comment <: a hashtag makes the rest of the line a comment. Python can house your notes~

tip.py - We're making a program to calculate the tip for a bill. <: You can do it!

How to calculate a tip: get bill, its 25$, tip is 5$
have bill*
    ask user for bill total* 
        we will prompt user to enter bill total as 00.00
        -store bill amount-
ask user for desired tip %
    we will prompt user to enter desired tip % as a number, ie 5=5% etc
    store tip % as a decimal
        how: convert whole number (tip% number entered by user) to a decimal, how: divide given value by 100. 20%=.2
-calculate tip % from bill total-   
    how: multiply bill total * tip % (as solved above) as a decimal. so 20.00 x .2 for 20% 
tell user amount as a whole number ie 00.00


! ! python specific notes ! !
    Python langauge details
operator - changes thing
    x = 5 changes x to five
function - gives thing
    print (function) = giving thing back to user
pass " "

'''
# userInput
userInputBillTotal=input("Please enter the total amount of your bill as 00.00: ")
#print(userInputBillTotal) to test
userInputTipPerc=input("Please enter the desired tip percentage as 00: ")

# calc
tipPercAsDec=float(userInputTipPerc)/100
tipAmount=float(userInputBillTotal)*(tipPercAsDec)
totalAmount=float(userInputBillTotal)+tipAmount

# output
print( )
print("=============================<3=============================")
print("Your tip is:",tipAmount)
print(" Your total bill is:",totalAmount)



  

