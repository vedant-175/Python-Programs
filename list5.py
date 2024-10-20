list1=input('enter list items:').split(',')
print(list1)
def delete_by_remove():
    element=input('Enter the element:')
    if element in list1:
        list1.remove(element)
        print('Update List',list1)
    else:
        print('Enter Valid Index')
delete_by_remove()
l1=input().split(',')
n=list(enumerate(l1))
print(n)
