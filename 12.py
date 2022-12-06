#print the smallest one in the given 3 integers
num1= int(input("enter first number"))
num2= int(input("enter second number"))
num3= int(input("enter third number"))
smallest=0
if num1<num2 and num1<num3:
    smallest=num1
elif num2<num3:
    smallest=num2
else:
    smallest=num3
print(smallest," is the smallest ofthe numbers.")
