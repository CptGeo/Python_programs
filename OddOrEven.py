"""
Ask the user for a number. Depending on whether the number is even or odd, print out 
an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
# Multiple functions are on not necessary but exist for exercise.

def oddoreven(number):
    if number==0:
        print("Number is equal to 0 \n")
    elif (number%2)==0:
        print("Number is even \n")
    elif (number%2)==1:
        print("Number is odd \n")

    return

def multOfFour(number):
    if (number%4)==0:
        print("The number is a multiple of 4\n")
    else:
        print("The number is NOT a multiple of 4\n")
    return

def divisionCheck(number,check):
    if (number/check)==1:
        print(" %d = %d\n" %(number,check) )
    else:
        print(" %d != %d\n" %(number,check))
    return


num=int(input("Please type an integer : \n"))
oddoreven(num)
multOfFour(num)
ch=int(input("Please type a number for the check: \n"))
divisionCheck(num,ch)
