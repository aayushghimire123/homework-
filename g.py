#7 reverse a list
arr = [1,2,3,4,5]
i = len(arr)-1
rev = []
while i >= 0:
    rev.append(arr[i])
    i -= 1
print(rev)