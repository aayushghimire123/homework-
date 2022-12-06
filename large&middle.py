
num1=1
num2=2
num3=3
def large():
    if num1 > num2 and num1 > num3:
        if num2>num3:
            return (num2)
        else:
            return (num3)
    elif num2 > num1 and num2 >num3:
        if num1 > num3:
            return (num1)
        else:
            return (num3)
    else:
        if num1 > num2:
            return (num1)
        else:
            return (num2)
print("middle=",large())