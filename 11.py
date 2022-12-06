#program which calculates the tax of an employee with the given condition 
s=int(input("enter your salary: "))
if s<20000:
    t=s-s*15/100
elif s>20000 and s==50000:
    t=s-s*25/100
elif s>50000 and s==100000:
    t=s-s*30/100
else:
    t=s-s*35/100
print("your tax is:",t)