#print multiplication table of 1,2,3,4,5,6,7,8
for i in range(1,9):
    print("\n\nMULTIPLICATION TABLE FOR %d\n" %(i))
    for j in range(1,9):
        print("%d X %d = %d" % (i, j, i*j))