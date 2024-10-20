def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n-1)
num=int(input())
if num < 0:
    print("Factorial not possible")
else:
    print(fact(num))
