n1=int(input("enter the number 1:"))
n2=int(input("enter the number 2:"))
n3=int(input("enter the number 3:"))
if n1>n2 and n1>n3:
    print('The Largest Number:',n1)
elif n2>n3 and n2>n1:
    print('The Largest Number:',n2)
elif n3>=n2 and n3>n1:
    print('The Largest Number:',n3)
elif n1==n2==n3:
    print("all the numbers are same")

