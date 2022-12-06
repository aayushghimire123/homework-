#Write a program to check two strings are anagram or not.
string1=input("enter a string")
string2=input("enter a string")
string2=string2.lower
string1=string1.lower
if(len(string1))==len(string2):
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if(sorted_string1 == sorted_string2):
        print(string1 , " and " , string2 + " are anagram.")
    else:
        print(string1 ," and " , string2 ," are not anagram.")

else:
    print(string1 , " and " , string2 , " are not anagram.")