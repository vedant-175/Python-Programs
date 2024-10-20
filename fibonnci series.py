n=int(input("Enter the number to get fiboncci series: "))
count=0
f0=0
f1=1
while(count<n):
    print(f0)
    num=f0 + f1
    f0=f1
    f1=num
    count=count+1
    
