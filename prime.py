a=int(input("enter a number"))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print("not a prime number")
    else:
        print("it is a prime number")