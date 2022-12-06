username="Ram"
password=1234
for i in range(3):
    username1=input("enter valid name")
    password1=int(input("enter valid pin"))
    if username==username1 and password==password1:
        print("logged in")
        break
    else:
        print("invalid ")
else:
    print("3 attempts finished")