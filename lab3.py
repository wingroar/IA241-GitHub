'''
lab 3
'''

#3.1
str_list =['a','d','e','b','c']
str_list.sort()
print(str_list)

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
print(str_list[2])

#3.5
my_list='a','123',123,'b','B','False',False,123,None,'None'
print(my_list)
print(set(my_list))
print(len(set(my_list)))
#there are 9 unique items

#3.6
print(len("This is my third python lab.".split()))

#3.7
num_list=[12,32,43,35]
num_list.sort()
print(num_list[0])
print(num_list[-1])

#3.8
game_board=[[0,0,0],[0,0,0],[0,0,0]]
game_board[1][1]=1
print(game_board)
