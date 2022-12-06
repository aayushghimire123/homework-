# Python program to check if number is Palindrome

def isPalindrome(n):  #user-defined function
    # calculate reverse of number
    reverse = 0
    reminder = 0
    while(n != 0):
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = int(n / 10)
    return reverse

# take inputs
num = int(input('Enter the number: '))

# calling function and display result
reverse = isPalindrome(num)
if(num == reverse):
  print(num,'is a Palindrome')
else:
  print(num,'is not a Palindrome')