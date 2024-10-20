def fact(n):
    if n ==0:
        return 1
    else:
        return n * count(n-1)
print(fact(0))
