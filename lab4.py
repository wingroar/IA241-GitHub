'''
lab4
'''

#3.1
my_dict={
'name':'tom',
'id':123
}
print(my_dict)

#3.2
print(my_dict.keys())
print(my_dict.values())

#3.3
my_dict['id']=321
print(my_dict)

#3.4
my_dict.pop('name')
print(my_dict)

#3.5
my_tweet={ 
"tweet_id":1138, 
"coordinates": (-75, 40), 
"visited_countries": ["GR", "HK", "MY"] 
}  
print(my_tweet)

#3.6
print(len(my_tweet['visited_countries']))

#3.7
my_tweet['visited_countries'].append('CH')
print(my_tweet)

#3.8
print('US' in my_tweet['visited_countries'])

#3.9
my_tweet['coordinates']=(81,45)
print(my_tweet)
