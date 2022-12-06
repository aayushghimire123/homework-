cost=int(input("enter your bike price:"))
if cost>=100000:
    t=(15/100)*cost
    print("your road tax is:",t)
elif cost>50000 and cost<=100000:
    t=(10/100)*cost
    print("your road tax is:",t)
else:
    t=(10/100)*cost
    print("your road tax is:",t)
    