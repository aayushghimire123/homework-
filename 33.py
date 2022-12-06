#accept the percentage and display the category according to the followig critria
pr=int(input("enter the percentage"))
if pr<40:
    print("your category is: failed")
elif pr>=40 and pr<55:
    print("your category is: fair")
elif pr>=55 and pr<65:
    print("your category is: good")
elif pr>=65 and pr<=100:
    print("your category is: excellent")
else:
    print("please enter correct percentage")