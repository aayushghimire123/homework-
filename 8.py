# A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. Ask user for their salary and year of service and print the net bonus amount.
y=int(input("enter the year of service"))
s=int(input("enter your salary"))
if y>5:
    print("yout net bonus is",(5/100)*s)