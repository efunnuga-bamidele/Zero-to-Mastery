#Dictionary

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

print(person)
print(person['kidsName'][0])
print(person.get('kidsName')[1])

# Creating dict using built in function

animal = dict(name = 'Dog', legs = 4)
print(animal)

print('country' in person)

print('country' in person.keys())

print('Efunnuga' in person.values())

person2 = person.copy() #copy a dictionary to another

person2.update({'age': 40}) # update the value of a key in the dictionary
print(person2)

print(person2.pop('age')) # delete the key in a dictionary
print(person2)