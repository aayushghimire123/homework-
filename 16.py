#program to check the number is armstrong or not 
num = int(input("Enter the number: ")) 
sum = 0 
temp = num 
for i in range(num): 
    digit = temp % 10 
    sum += digit ** 3
    temp //= 10
    if (num == sum):
     print("Armstrong number") 
     break
else: 
    print("Not an Armstrong number")