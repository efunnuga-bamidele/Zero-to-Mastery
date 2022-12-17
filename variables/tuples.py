#Tuples

my_tuple = (1, 2, 3, 4, 5)

#tuples are immutable on like list

print(my_tuple)
print(5 in my_tuple)

new_tuple = my_tuple[1:2]
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)

print(x)
print(y)
print(z)
print(other)

print(len(my_tuple))
print(my_tuple.index(3))