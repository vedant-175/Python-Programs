n1=int(input('enter the no.1:'))
n2=int(input('enter the no.2:'))
n3=int(input('enter the no.3:'))
n4=int(input('enter the no.4:'))
if n1>n2 and n1>n3 and n1>n4:
    print('n1 is greatest')
if n2>n3 and n1>n4:
    print('n2 is greatest')
if n3>n4:
    print('n3 is greatest')
else:
    print('n4 is greatest')
