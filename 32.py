#accept the data and calculate the percentage of class attended and if percentage is less than 75 than student will not be able to sit in exam
nd=int(input("enter total number of working days"))
na=int(input("enter number of days absent"))
per=(nd-na)/nd*100
print("your attandence is: ",per)
if per<75:
    print("you are not eligible for exam")
else:
    print("you are eligible for writing exam")
    