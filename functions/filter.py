#filter
# remove any item that returns false

my_list = [1,2,3]
user_names = ['bamidele', 'samuel', 'matilda', 'bola', 'janet']

def only_odd(item):
    return item % 2 != 0

def remove_name(item):
    return item[0] == 'b'


print(list(filter(only_odd, my_list)))
print(my_list)

print(list(filter(remove_name, user_names)))
print(user_names)