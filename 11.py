#11  python program that accept a strig and calculate the numbers of digits and letters
a="hello123"
digit=0
letter=0
for i in a:
     if i.isdigit():
         digit=difit +1
     elif i.isalpha():
         letter=letter+1
     else:
         pass
     print(digit)
     print(letter)
