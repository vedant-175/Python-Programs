def power(base,exp):
    if exp==0:
        return 1
    elif exp==1:
        return base
    else:
        return base*power(base,exp-1)
base=int(input())
exp=int(input())
print(power(base,exp))
    
