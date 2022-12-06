age1 =int(input("enter first age"))
age2= int(input("enter second age"))
age3=int(input("enter third age"))
if age1>age2 and age1>age3:
    print("olddest is: ", age1)
elif age2>age1 and age2>age3:
    print("oldest is: " ,age2)
else:
    print("oldest is: ",age3)
if age1<age2 and age1<age3:
    print("smallest is: ", age1)
elif age2<age1 and age2<age3:
    print("smallest is: " ,age2)
else:
    print("smallest is: ",age3)