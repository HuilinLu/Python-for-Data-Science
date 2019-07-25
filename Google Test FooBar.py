# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:07:27 2019
FooBar Test from Google
@author: D17911
"""

### Level 1: Minion Task
counts = dict()
data = list(input('Input Test Data: '))

n = int(input('Input n here: '))

def answer(data, n):
    new_list = list()
    for number in data:
        counts[number] = counts.get(number, 0) + 1  
    for key, values in counts.items():
        if values <= n:
            try:
                key = int(key)
            except:
                continue
            new_list.append(key)
        else:
            continue
    print(new_list)
    
    
### Level 2
"""  Level 2: En_route_salute """
s = input('Put the road here: ')
string = list(s)
sum = 0
for strings in string:
    if str(strings)  == '>' :
        atpos = s.find(strings)
        remain=list(s[atpos+1:])
        count = 0
        for remains in remain:
            if str(remains) == '<' :
                count = count + 1
        sum = sum + count
print(2*sum)


"""  Level 2: numbers_station_coded_messages """
l=[1, 2, 3]   
for number in l:
    ind = l.index(number)
    print(ind)
    
    
    
    
    
    







