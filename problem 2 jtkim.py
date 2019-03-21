#jtkim
#3/7/2019

#checks if two user inputs are less than or greater than or equal to 10

number1 = int(input("Enter in number 1: "))
number2 = int(input("Enter in number 2: "))

def numberCheck(n1, n2):
    if n1 + n2 == 10:
        print("Equal")

    elif n1 + n2 > 10:
        print("Greater than")

    else:
        print("Less than")

print(numberCheck(number1, number2))
