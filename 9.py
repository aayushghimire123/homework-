#9. Given number is prime or not:
a=int(input("Enter a number; "))
if a>1:
     for i in range(2,a):
         if a%i==0:
             print("It is not a prime number")
             break
     else:
         print("It is a prime number")
else:
     print("It is not a prime number")