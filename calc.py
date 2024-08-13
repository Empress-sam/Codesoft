import math

def addf(num1,num2):
    g=num1+num2
    print("")
    print("----------------------------------------")
    print("")
    print(num1," + ",num2," = ",g)
    input()

    print("Enter e to exit")
    print("")
    print("Enter 0 to Continue")
    print("")
    
    choice_in_function = input("Enter Your Choice : ")

    if choice_in_function == "e" or choice_in_function == "E":
        exit

    elif choice_in_function == "0":
        Main_Code()

    else:
        print("")
        print("Invalid Choice")
        print("")
        Main_Code()

def differencef(num1,num2):
    h=num1-num2
    print("")
    print("----------------------------------------")
    print("")
    print(num1," - ",num2," = ",h)
    input()

    print("Enter e to exit")
    print("")
    print("Enter 0 to Continue")
    print("")
    
    choice_in_function = input("Enter Your Choice : ")

    if choice_in_function == "e" or choice_in_function == "E":
        exit

    elif choice_in_function == "0":
        Main_Code()

    else:
        print("")
        print("Invalid Choice")
        print("")
        Main_Code()

def productf(num1,num2):
    i=num1*num2
    print("")
    print("----------------------------------------")
    print("")
    print(num1," * ",num2," = ",i)
    input()

    print("Enter e to exit")
    print("")
    print("Enter 0 to Continue")
    print("")
    
    choice_in_function = input("Enter Your Choice : ")

    if choice_in_function == "e" or choice_in_function == "E":
        exit

    elif choice_in_function == "0":
        Main_Code()

    else:
        print("")
        print("Invalid Choice")
        print("")
        Main_Code()

def divisionf(num1,num2):
    j=num1/num2
    print("")
    print("----------------------------------------")
    print("")
    print(num1," / ",num2," = ",j)
    input()

    print("Enter e to exit")
    print("")
    print("Enter 0 to Continue")
    print("")
    
    choice_in_function = input("Enter Your Choice : ")

    if choice_in_function == "e" or choice_in_function == "E":
        exit

    elif choice_in_function == "0":
        Main_Code()

    else:
        print("")
        print("Invalid Choice")
        print("")
        Main_Code()


def floatdivf(num1,num2):
    l=num1//num2
    print("")
    print("----------------------------------------")
    print("")
    print(num1," // ",num2," = ",l)
    input()

    print("Enter e to exit")
    print("")
    print("Enter 0 to Continue")
    print("")
    
    choice_in_function = input("Enter Your Choice : ")

    if choice_in_function == "e" or choice_in_function == "E":
        exit

    elif choice_in_function == "0":
        Main_Code()

    else:
        print("")
        print("Invalid Choice")
        print("")
        Main_Code()



def Basic_Code():

    print("Enter (1) for Addition")
    print("Enter (2) for Substraction")
    print("Enter (3) for Multiplication")
    print("Enter (4) for Division")
    print("Enter (5) for Float Division")
    print("")
    print("Enter (0) to Go Back")
        
  
    print("")
    print("----------------------------------------")
    print("")

    basic_calculation = input("Enter Your Choice : ")
    print("")


    if basic_calculation == "1":

        num1=float(input("Enter First Number : "))
        num2=float(input("Enter Second Number : "))
        print("")
        addf(num1,num2)

    elif basic_calculation == "2":

        num1=float(input("Enter First Number : "))
        num2=float(input("Enter Second Number : "))
        print("")
        differencef(num1,num2)

    elif basic_calculation == "3":

        num1=float(input("Enter First Number : "))
        num2=float(input("Enter Second Number : "))
        print("")
        productf(num1,num2)

    elif basic_calculation == "4":

        num1=float(input("Enter First Number : "))
        num2=float(input("Enter Second Number : "))
        print("")
        divisionf(num1,num2)

    elif basic_calculation == "5":
        num1=float(input("Enter First Number : "))
        num2=float(input("Enter Second Number : "))
        print("")
        floatdivf(num1,num2)

    elif basic_calculation == "0":
        Main_Code()

    else:
        print("Wrong Input")
        print("")
        Basic_Code()

def Main_Code():
    print("")
    print("")
    print("----------------------------------------")
    print("")
    print("To start calculation press 1")
    print("To exit press 2")
    print("")
    print("")

    calculation_type = input("Enter Your choice: ")
    print("")


    if calculation_type == "1":
        Basic_Code()


   
   

    
   
Main_Code()

