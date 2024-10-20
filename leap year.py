x=int(input("enter year:"))
if x%4==0:
    print('It is a leap year')
elif x%100==0:
    print("it is century year")
else:
    print("it is not leap year")
