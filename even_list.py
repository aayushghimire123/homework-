
number= int(input("enter an integger number"))
even_count, odd_count = 0, 0
 
# iterating each number in list
for number in list1:
     
    # checking condition
    if number % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
         
print("Even numbers in the list: ", even_count)
