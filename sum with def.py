def all_sum(*args):
    sum=0
    for num in args:
        sum=sum+num
    print(sum)
a=10
b=2
c=3
d=4
e=5
all_sum()
all_sum(d,e)
all_sum(a,b,c)
all_sum(a,b,c,d,e)
all_sum(c,d)
