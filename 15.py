#program to check the given number is palindrome or not 
number=input("Enter any number/word :")
i=0
for i in range(len(number)):
    if number[i]!=number[-1-i]:
        print('It is not a palindrome')
        break
else:
    print('It is a palindrome')