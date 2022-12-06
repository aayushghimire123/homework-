#A company decided to give bonus to employee according to following criteria:
salary =int(input("Enter your salary > "))
service= int(input("Enter the year of service > "))
if service > 10:
 net_bonus= (10 / 100) * salary
if service >=6 and service <=10:
 net_bonus = (8 / 100) * salary
if service < 6:
 net_bonus = (5 / 100) * salary
print("Net Bonus is ", net_bonus)