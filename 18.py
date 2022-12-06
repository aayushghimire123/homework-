#program to check the given number is perfect number 
input_num = int(input("Enter the value:"))
result = 0
for m in range(1, input_num ):
    if(input_num  % m == 0):
        result = result + m
if (result == input_num ):
    print("Yes it is a Perfect number!")
else:
    print("No ,the value is not a Perfect number!")