#8. Program to count the tottal number of digits in a number:
# digit=0
# a=int(input("Enter number: "))
# for i in str(a):
#     if i.isdigit():
#         digit=digit+1
#     else:
#         pass
# print(digit)

#OR

digit=0
a=input("Enter number: ")
for i in a:
     if i.isdigit():
         digit=digit+1
     else:
         pass
print(digit)


