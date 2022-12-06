#accept any city from user and display monument of the city 
city=input("enter city")
if city.upper()=="DELHI":
    print("red fort")
elif city.upper()=="AGRA":
    print("taj mahal")
elif city.upper()=="JAIPUR":
    print("jal mahal")
else:
    print("enter a valid city")
    
