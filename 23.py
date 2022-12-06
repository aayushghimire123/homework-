#to accpet two numbers and mathematical operators and perform operation accordingly
n1=float(input("enter a number[N1]:"))
n2=float(input("enter second number[N2]:"))
op= input("enter the desired mathematical operator:")
if op=="+":
    print("you've chosen to add the numbers")
    print(n1+n2,"is the sum of the numbers")
elif op=="-":
    print("you have chosen to subtract the number")
    c=input("N1-N2 or N2-N1?:")
    if c=="N1-N2" or c=="n1-n2":
        print(n1-n2,"is the difference of the numbers")
    else:
        print(n2-n1,"is the differnec of the numbers")
elif op=="*":
    print("you have chosen to multiply the numbers")
    print(n1*n2,"is the product of the numbers")
elif op=="/":
    print("you have chosen to divide the numbers")
    c=input("N1/N2 OR N2/N1")
    print(n1/n2," isthe quotient of division")
else:
    print(n2/n1,"is the quotient of division")
    