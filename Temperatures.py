import sys
import math
r=5527
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if (abs(t)<abs(r)):
        r = t
    elif abs(t) == abs(r):
        r = abs(t)

if r==5527:
    print("0")
else:
    print(r)
