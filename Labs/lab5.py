'''
lab5
'''

#3.1
alien_color='green'

if alien_color=='green':
    print('you got 5 points')

#3.2
alien_color='red'
if alien_color=='green':
    print('you got 5 points')
else:
    print('you got 10 point')

#3.3
favorite_fruits=['apple','banana','orange']
if 'orange' in favorite_fruits:
    print('you really like orange')
    
#3.4
age=90
if age<10:
    print('kid')
elif age<20:
    print('teenager')
else:
    print('adult')
    if age>=60:
        print('elder')