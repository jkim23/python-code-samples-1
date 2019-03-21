#jt kim
#2.29.2019
#compute radius of circle 
#radius = int(input("Enter radius for your circle: "))
#area_of_circle = (radius * 3.14) * radius
#print ("Your circle is: ", area_of_circle)

def areaOfCircle(radius):
    area = (radius ** 2) * 3.14
    return area

print("the area of the circle is ", areaOfCircle(10))

print("the area of the circle is ", areaOfCircle(20))

print("the area of the circle is ", areaOfCircle(30)) 
