#write a program to calculate gross rate on the basis of hrs and rate per hrs work for 
hrs=int(input('hours:'))
rate=int(input('rate:'))
y=hrs%40
print(y)
if hrs>40:
    print((hrs-y)*rate+(y*rate*1.5))
else:
    print(hrs*rate)
