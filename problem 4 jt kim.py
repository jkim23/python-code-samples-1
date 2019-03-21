#jtkim
#3/7/2019

#takes a year and returns true if year is a leap year

year = int(input("Enter in year number: "))

def numberCheck (year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        return True
    
print(numberCheck(year))

("it is not a leap year")
("it is a leap year")
