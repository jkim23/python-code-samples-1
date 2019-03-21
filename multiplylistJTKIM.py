#jtkim
#2.28.19
#multiplies all values in a list

def multiplyList (numbers):
    total = 1
    for n in numbers:
        total = total*n
    return(total)

n= [2, 5, 3, -8, 10]

print(multiplyList(n))
