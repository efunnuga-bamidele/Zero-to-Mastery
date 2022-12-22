# reduce function

#lambda expression
# Onetime anonimus function
# lambda param: action(param) 

from functools import reduce


my_list = [1,2,3]

def multiply_by2(item):
    return item * 2

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))


print(list(map(lambda item: item * 2, my_list)))