#python code to print n consecutive integers 
from __future__ import print_function

N = int(input())
print(*range(1,N+1), sep='') (# * is used as unpacking operator to unpack the elements in the input array)
