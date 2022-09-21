#Ask a user and check he/sh is elegible for vote (must be greater then 19) or not. 

age=int(input("Enter age:"))

if age>=18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voiting")

