bag = dict()
bag['candies'] = 10
bag['lipstick'] = 1
bag['money'] = 100
bag['keys'] = 3
print(bag)

bag1 = {'candies': 20, 'money': 10, 'keys': 13, 'lipstick': 5}
print bag1

#try to find the key in the dictionary
print('candies' in bag1)


#from list to dictonary
name_dict=dict()
name_list=['pippo','pluto','minnie','paperino','minnie','pippo']
for name in name_list:
    if name in name_dict:
        name_dict[name] = name_dict[name]+1
    else:
        name_dict[name] = 1
print name_dict

#in a more elegant manner, we can use the method get of dictionaries that return
#the value for the key or a default value if the key is not present
name_dict=dict()
for name in name_list:
        name_dict[name] = name_dict.get(name,0)+1
print name_dict

jjj=list(name_dict) #converts the dictionary in a list
print(jjj)          #it lost the values

#keys and values are methods of dictionaries
#items return the key pair values
print (name_dict.keys())
print (name_dict.values())
print(name_dict.items())

for k,v in name_dict.items():
    print (k,v)
