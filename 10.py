#ask user to enter marks and print the corresponding grade
marks= int(input("entyer marks"))
if marks<25:
    print("f")
elif marks>=25 and marks<45:
    print("E")
elif marks>=45 and  marks<50:
    print("D")
elif marks>=50 and marks<60:
    print("C")
elif marks>=60 and marks<80:
    print("B")
else:
    print("A")
    