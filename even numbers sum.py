num=int(input("num = "))
sum=0
count=0
while num!=0:
    if(num%2==0):
        sum=sum+num
        count=count+1
    num=num-1
print("sum:",sum)
print("average:",sum/count)
