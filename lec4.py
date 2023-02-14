'''
lec4
dict and turple
'''

my_tuple=('a','b','c','d','e')

#my_tuple[0]='f' does not work
print(my_tuple[0])


#Dictionary


my_car={
'color':'red',
'maker':'toyota',    
'year':2015
}
print(my_car)
print(my_car['color'])
print(my_car['maker'])

print(my_car.items())

print(my_car.keys())

print(my_car.get('color'))
print(my_car['color'])
#these are pretty much the same

my_car['model']='venza'
print(my_car)

my_car['year']=2020
print(my_car)

print(len(my_car))

print('color' in my_car)

print('red' in my_car.values())
#must use .values because 'in' fucntion will only check for keys unless you specify you are looking for values

