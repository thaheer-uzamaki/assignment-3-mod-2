from math import tan, pi
n=int(input("number of sides: "))
s=float(input("the length of a side: "))
a=n*(s ** 2)/(4 * tan(pi/n))
print("The area of the polygon is: ",a)
