#Accept the percentage from the user and display the grade according to the following criteria:

marks= int(input("entyer marks"))
if marks<25:
    print("D")
elif marks>=25 and marks<45:
    print("C")
elif marks>=45 and  marks<50:
    print("B")
elif marks>=50 and marks<60:
    print("B+")
elif marks>=60 and marks<80:
    print("A")
else:
    print("A+")
    