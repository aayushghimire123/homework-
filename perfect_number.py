# Python program to check perfect number using function

def perfect_numbers(N):  
   sum = 0
   for i in range(1,N): 
      if(N%i == 0):
         sum = sum+i 
   return sum 
N = int(input("enter a number"))
if(N == perfect_numbers(N)): 
   print(N, "is a perfect number") 
else: 
   print(N, "is not a perfect number") 