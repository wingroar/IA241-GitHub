'''
lec3

list and set
'''

my_list=[1,2,3,4,5]

print(type(my_list))

my_nested_list=[1,2,3,my_list]
print(my_nested_list)

my_list[0]=6
print(my_list)

print(my_list[:])   # if you leave both spaces blank it prints out entire list if you leave first space blank it starts from 0 and if you leave second space blank it goes all the way till the end

x,y,z=['a','b','c']
print(x)           #each value is assigned in order x=a y=b z=c

my_list.append(7)
print(my_list)

my_list.remove(5)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list+[8,9])

my_list.extend([8,9])
print(my_list)

print(len(my_nested_list))

print('hello world'[0:5])

my_letters=['a','a','b','c']
print(my_letters)

my_letters_set=set(my_letters)

print(list(my_letters_set)[0])