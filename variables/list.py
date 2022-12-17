li1 = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
    ]

# Data Structure

# list slicing
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])

amazon_cart[0] = 'textbooks'
print(amazon_cart)

# modifying list memory location

# new_cart = amazon_cart

# copy list to another without modifying the memory location

new_cart = amazon_cart[:] 

new_cart[0] = 'laptop'
print(new_cart)
print(amazon_cart)


# Matrix
# Multi dimensional list
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]

print(matrix[0][2])

# List Methods

basket = [1,2,3,4,5]

# adding method modifies original list
basket.append(6) # add list to end of list
basket.insert(5, 10) # collect position index and value to add to list
basket.extend([7, 8, 9]) # add multiple values to list
print(basket)

#removing 
basket.pop() #remove last value in the list
basket.pop(0) # remove by index
basket.remove(10) #remove the value located in the list
# basket.clear() #remove the entire list values

print(basket)

alpha = [ 'a', 'b', 'c', 'd', 'e', 'd']

print(alpha.index('d')) #returns the index of the value
print(alpha.index('d', 0, 4)) #search for value between 0 - 4 index range and return index of value if found

print('g' in alpha) # check if value exist in list and return True or False

print(alpha.count('d')) # Return the number of times a value appears in a list
alpha.sort() 
alpha.reverse()
print(alpha)
print(len(alpha))

print(alpha[::-1]) #use slicing to reverse a list but not modify the original list

# print(list(range(1,100))) #generate a list between the range
# print(list(range(101))) #generate a list between the range

sentence = ' '.join(['Hi', 'my', 'name', 'is', 'Bamidele'])

print(sentence)

# list unpacking
a, b, c, *other, d = [1,2,3,4,5,6,7,8,9]
 
print(a)
print(b)
print(c)
print(other)
print(d)



