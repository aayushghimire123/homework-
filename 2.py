# Accept the age of 4 people and display the youngest one.
age1=int(input("enter 1st age:"))
age2=int(input("enter 2nd age:"))
age3=int(input("enter 3rd age:"))
age4=int(input("enter 4th age:"))
if age1<age2 and age1<age3 and age1<age4:
    print("youngest one is:",age1)
elif age2<age1 and age2<age3 and age2<age4:
    print("youngest one is:",age2)
elif age3<age1 and age3<age2 and age3<age4:
    print("youngest one is:",age3)
else:
    print("youngest is:",age4)
    