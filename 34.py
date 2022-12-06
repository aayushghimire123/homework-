#accept the age, sex and number of days and display accordingly 
age= imt(input("enter your age:"))
sex=input("enter sex(m/f)")
nd=int(input("enter number of days"))
if age>=18 and age<30 and sex.upper()=="M":
           amt=nd*700
           print("total wages is: ",amt)
elif age>=18 and age<=30 and sex.upper()=="F":
   amt=nd*750  
   print("Total wage is: ",amt)
elif age>=30 and age<=40 and sex.upper()=="M":
    amt=nd*800
    print("total wages is: ",amt) 
elif age>=30 and age<=40 and sex.upper()=="F":
    amt=nd*850
    print("total wages is: ", amt)
else:
    print("enter the appropriate age")
                                                                