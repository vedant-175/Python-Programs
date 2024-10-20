import math as m
side1=int(input())
side2=int(input())
hypo=int(input())
if pow(hypo,2)==pow(side1,2)+pow(side2,2):
    print("right angle triangle is possible")
else:
    print("right angle triangle is not possible")
