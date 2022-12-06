m=int(input("enter marks of math: "))
n=int(input("enter marks of nepali:"))
e=int(input("enter marks of english:"))
s=int(input("enter marks of science:"))
def calculatesum():  #calculates sum
    sum=m+n+e+s
    return sum
print("your total marks is ",calculatesum())

def calculateper():   #calculates percentage
    percent=((m+n+e+s)/400)*100
    return percent
print(f"your percent is {calculateper()}%",)

def calculateres():               #calculates result
    percent=((m+n+e+s)/400)*100
    if percent< 40: 
        result="failed"
    if(m<40 or n<40 or e<40 or s<40):
        result="fail"   
    else:
        result="passed"
    return result
print(calculateres())