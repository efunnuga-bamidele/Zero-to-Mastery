# for loop

for item in 'Zero to Mastery':
    print(item)

for num in {1, 2, 3, 4, 5}:
    print(num)

# nested loops
for k in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(k, x)

print('\n')
person ={
    'firstName' : 'Bamidele',
    'lastName' : 'Efunnuga',
    'age' : 33,
    'state' : 'Ogun',
    'country' : 'Nigeria',
    'isMarried' : True,
    'haveKids' : True,
    'kidsName' : ['Samuel', 'Matilda'] 
}

for detail in person:
    print(detail)

print('\n')

for detail in person.items():
    print(detail)

print('\n')

for key, value in person.items():
    print(key, value)

print('\n')

for detail in person.values():
    print(detail)

print('\n')

for detail in person.keys():
    print(detail)


