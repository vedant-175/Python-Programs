def add():
    add=a+b
    print('sum:',add)
a=int(input("a:"))
b=int(input("b:"))
add()

def sub():
    sub=a-b
    print('sub:',sub)
a=int(input("a:"))
b=int(input("b:"))
sub()

def multiply():
    mul=a*b
    print('multiplication:',mul)
a=int(input("a:"))
b=int(input("b:"))
multiply()

def division():
    
    if b==0:
        print('undefined')
    else:
        print('Division:',a/b)
a=int(input("a:"))
b=int(input("b:"))
division()

