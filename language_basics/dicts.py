D = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(D))
print(type(D))

# ACCESS 
print(D['model'])
print(D.get('model'))

# ACCESS - return a default value 
print(D.get('color', 'blue'))

print(D)

# get keys, values and items
k = D.keys()
v = D.values()
items = D.items()

print(k)
print(v)
print(items)

# addng a new item updats k, v & items
D['seat_color'] = 'tan' 

print(k)
print(v)
print(items)

#check if key exists
print('model' in D)
print('zzz' in D)

# two ways to make updates
D['year'] = 2018
print(D['year'])

D.update({'year': 2020})
print(D.get('year'))

D.update({'year': 2033, 'seat_color': "blue", 'wheel': 'cool'})
print(D.get('year'), D.get('seat_color'), D['wheel'])

# use 'pop' to remove items
D.pop('wheel')
print(D)

# or just call del
del D['seat_color']
print(D)

# loop through D
for x in D:  # same as for x in D.keys()
  print(x)

for tpl in D.items():
  print(tpl)

# make a copy ( not a reference of D )
E = D.copy()
F = dict(D)

print(E == D)
print(E is D)
D2 = D
print(D2 is D)

# use 'clear' to empty the dict
D.clear()
print(D)
