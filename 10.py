#10  python program to count the number of even and odd numbers from a series of number.
list1 = [10, 21, 4, 45, 66, 93, 1]
even=0
odd = 0
for num in list1:
     if num % 2 == 0:
         even += 1
     else:
         odd += 1
print("Even numbers in the list: ", even)
print("Odd numbers in the list: ", odd)