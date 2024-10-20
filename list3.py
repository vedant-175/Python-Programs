list1=input().split(',')
print(list1)
def delete_by_del():
    index=int(input('Enter the index you want to delete?'))
    if index<=len(list1)-1:
        del list1[index]
        print('updated List is: ',list1)
    else:
        print('Enter Valid Index')
delete_by_del()
