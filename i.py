#given number is prime or not
num=int(input("Enter a number: "))
check=True
i=2;
while i*i<=num:
    if(num%i==0):
        check=False
        break
    i+=1

if(check and num!=1):
    print(str(num)+" is a Prime Number")
else:
    print(str(num)+" is not a Prime Number")