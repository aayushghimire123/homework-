# ask a num from user and filter odd and add into odd list 

number= int(input("enter an integer number"))
 
even_count, odd_count = 0, 0
 

for number in list1:
     
 
    if number % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
print("Odd numbers in the list: ", odd_count)