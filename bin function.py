def Bin(n):
    if n>=1:
        Bin(n//2)
    print(n%2,end ='')
Bin(10)
