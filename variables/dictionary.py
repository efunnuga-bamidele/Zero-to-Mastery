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