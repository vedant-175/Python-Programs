import math as m
x=int(input())
deg=m.degrees(x)
rad=m.radians(x)
if x > 360:
    print("enter a valid angle")
else:
    print(f"{deg:.2f}")
