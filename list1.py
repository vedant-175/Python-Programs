list1=input('enter element:').split(',')
print(list1)
int_list=[int(x) for x in list1]
print('Integer list: ',int_list)
tuple1=tuple(int_list)
print("This is my first tuple:",tuple1)
tuple2=tuple(int_list)
print('this is my second tuple:',tuple2)
