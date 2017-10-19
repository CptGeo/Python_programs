

#-------FUNCTIONS-------
#Definition of the printMessage function which asks for a number for how many times to display a specific message.
def printMessage(named,aged,yeard):
    i=0
    numberTimes=int(input("How many times do you want to display the message?"))
    print(numberTimes)
    if numberTimes>0:
        for i in range(0,numberTimes) :
            print("Your name is %s , your age is %d , the year is %d and you will be 100 on year %d" %(name,age,year,((year-age)+100)))
    elif numberTimes==0:
        print("Goodbye!")
        return 0
    return 0



#Definition of the printMessageWithEnter function which displays the message when ENTER is pressed, or it exits when the user types 'exit'.
def printMessageWithEnter(named,aged,yeard):
    inputVar=input("Press ENTER to display message or type EXIT to terminate")
    while inputVar !="" and inputVar.lower()!="exit":
        inputVar=input("Invalid Command! Please press ENTER to continue or type EXIT to terminate ")
    if inputVar=="":
        while inputVar=="":
            print("Your name is %s , your age is %d , the year is %d and you will be 100 on year %d" %(name,age,year,((year-age)+100)))
            inputVar=input("Press ENTER to display message or type EXIT to terminate")
            while inputVar !="" and inputVar.lower()!="exit":
                inputVar=input("Invalid Command! Please press ENTER to continue or type EXIT to terminate")
    elif inputVar.lower()=="exit":
        print("Exiting...")
        return
    print("Exiting...")


#--------MAIN PROGRAM-------
#Importing the datetime class from the datetime module so that the program is a bit more flexible after time (Because we can see the specific date and time with it).

from datetime import datetime

name=input("Please type your name : ")
#Checking if name is entered properly with .isalpha class which is False when the string contains numbers.
while name.isalpha()==False:
    name=input("Your name cannot contain numbers.\nPlease try again : ")

age=int(input("Please type your age :"))
now = datetime.now()
year=int(now.year)
print("Your name is %s , your age is %d , the year is %d and you will be 100 on year %d" %(name,age,year,((year-age)+100)))
printMessage(name,age,year)
printMessageWithEnter(name,age,year)
