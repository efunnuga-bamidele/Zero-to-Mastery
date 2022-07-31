#Fundamental Data types

int #whole number data types
# print(type(2 + 6))
# print(2 - 4)
# print(3 * 4)
# print(type(2 / 4))

# print(2 ** 3)
# print(6 // 4)
# print(6 % 4)
float #decimaal number data types
# bool
# str
# list
# tuple
# set
# dict
# complex


#Classes -> Custom types


#Specialized Data Types

#->Modules
None

#math functions
# print(round(3.9832093, 2))

# print(abs(-20))
# print(bin(3))
# print(int("0b11", 2))
#Operator precedence

# Naming Variables

#Statement vs expression

#augmented assignment operation

# some_value = 5
# some_value = some_value + 2  # one method of addition
# some_value += 2  #augmented assignment approach

# print(some_value)


#Strings

# long_string = '''
# WOW
# 0 0
# ---
# '''

# print(long_string)

#formatted strings

# name = "Johnny"
# age = 55

# print(f"hi {name}. You are {age} years old")
# print('hi {}. You are {} years old'.format(name, age))

# selfish = '01234567'
#index     01234567

# slicing 
# string[start:stop:step]

# reverse_name = 'Bamidele Efunnuga'
# print(reverse_name[::-1])
# print(selfish[::-1]) #Reverse the string
# print(len(reverse_name))


# quote = "to be or not to be"
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))

# # Booleans

# name = 'Andrei'
# is_cool = False
# is_cool = True

# if is_cool:
#     print('Profile was liked')
# else:
#     print('Profile was not liked')


# Data Structure
# List

li1 = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a', True]

amazon_cart = ['notebooks', 'sunglasses', 'Toys', 'Grapes']

print(amazon_cart)
# list indexing
print(amazon_cart[2])
# List slicing
print(amazon_cart[0:2])

# list mutable
amazon_cart[0] = 'laptop'
print(amazon_cart)