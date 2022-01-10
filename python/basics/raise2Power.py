import math

#Assign values to x and n
x = input("What is your x? ")
n = input("What is your n? ")

#Cast into floats
x = float(x)
n = float(n)

#Method 1
print("Using x ** n:")
power = x ** n
print("%5.2f to the power %5.2f is %5.2f\n" % (x,n,power))

#Method 2
print("Using pow(x,n):")
power = pow(x,n)
print("%5.2f to the power %5.2f is %5.2f\n" % (x,n,power))

#Method 3
print("Using math.pow(x,n):")
power = math.pow(x,n)
print("%5.2f to the power %5.2f is %5.2f\n" % (x,n,power))
