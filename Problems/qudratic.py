from math import sqrt

a = float(input("Write the first number here: "))
b = float(input("Write the second number here: "))
c = float(input("Write the third number here: "))

r = b*b - 4*a*c

if r>0:
    x1 = (-b+sqrt(r))/2*a
    x2 = (-b-sqrt(r))/2*a
    print("There are two roots.")
    print("The roots are", x1, "and", x2)
elif r==0:
    x = -b/2*a
    print("There is one root.")
    print("The root is ", x)
else:
    print("There are no real roots.")