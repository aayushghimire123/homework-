for row in range(5):
 for column in range(9):
  if (column==0 and row!=3) or ((column==1 or column==2) and (row!=1 and row!=3)) or (column==3 and row!=1) or (column==5) or ((column==6 or column==7) and (row==0 or row==2)) or (column==8):
     print("*",end=" ")
 else:
   print(end=" ")
print()