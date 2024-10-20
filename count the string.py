a=input()
b=input()
d=len(a)
count=0
for i in range(0,d+1):
    if a[i] == b:
        count=+1
print('count:',count)
