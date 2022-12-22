# def hello():
#     print('hellloooooooooooooooo!')

# greet = hello

# del hello

# hello()

# print(greet())

#Higher Order Function HOC
# accepts or return other function

# def hello(func):
#     func()

# def greet():
#     def func():
#         return 5
    
#     return func


#Decorator


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****************')
        func(*args, **kwargs)
        print('*****************')
    return wrap_func


@my_decorator

# def holla():
#     print('Helllllooooooooo!')

# holla()

def hello(greeting):
    print(greeting)

hello("helloooooooo")