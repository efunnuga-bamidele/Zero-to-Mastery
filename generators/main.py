# generators

def generator_function(num):
    for i in range(num):
        yield i * 2
        # yield pauses te function until next is called




# for item in generator_function(1000):
#     print(item)

g = generator_function(100)
next(g)
next(g)
next(g)
print(next(g))


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(1*2)
#     return result