#formatted strings

name = 'Johnny'
age = 55

print("Hi "+ name +". You are "+ str(age) +' years old\n');

print(f'Hi {name}. You are {age} years old\n')

print('Hi {}. You are {} years old\n'.format(name, age))

# Indexing

selfish = '0123456789'
          #0123456789

# [start:stop:stepover]
print(selfish[0:8:2])