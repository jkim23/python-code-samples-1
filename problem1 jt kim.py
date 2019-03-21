#jtkim
#3/7/2019

#checks if two user inputs are equal

number1 = int(input("Enter in number 1: "))
number2 = int(input("Enter in number 2: "))

def numberCheck(n1, n2):
    if n1 == n2:
        print ("True")
        return True
    else:
        print ("false")
        return False

print(numberCheck(number1, number2))
      
