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





