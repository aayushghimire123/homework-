#to accept the marks in 4 subjects and display total marks, percentage and garde 


marksa= int(input("enter marks in english"))
marksb= int(input("enter marks in nepali"))
marksc= int(input("enter marks in science"))
marksd= int(input("enter marks in maths"))
t=(marksa+marksb+marksc+marksd)
p=(t)/4
if p>70:
    print("distinction")
elif p>60 and p<60:
    print("first division")
elif p>40:
    print("pass")
else:
    print("fail")
print(p,"is the percentage")
print(t,"is the total marks")
