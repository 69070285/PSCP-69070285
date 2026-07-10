"""OverlapCircle"""
from math import sqrt
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
d = sqrt(((x1-x2)**2)+((y1-y2)**2))
if r1 > d/2 or r2 > d/2:
    print("overlapping")
else:
    print("no overlapping")
