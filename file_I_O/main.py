# Method One
# my_file = open('text.txt')

# print(my_file.readlines())
# print(my_file.readline())
# my_file.seek(0)
# print(my_file.read())

# my_file.close()


# Method Two
with open('app\sad.txt', mode='r') as my_file:
    # text = my_file.write('Hey it\'s me bamidele efunnuga')
    # text = my_file.write('My name is bamidele efunnuga')
    # print(text)
    # my_file.seek(0)
    print(my_file.read())