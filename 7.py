#Accept the number of days from the user and calculate the charge for library according to following:
nd=int(input("enter number of days"))
if nd<=5:
    amt=nd*2
elif nd>=6 and nd<=10:
    amt=nd*3
elif nd>=11 and nd<=15:
    amt=nd*4
else:
    amt=nd*5
print("total amount to pay is: ",amt)