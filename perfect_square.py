#perfect square
from math import sqrt
def solve(n):
   sq_root = int(sqrt(n))
   return (sq_root*sq_root) == n
n = int(input("enter a number"))
print (solve(n))