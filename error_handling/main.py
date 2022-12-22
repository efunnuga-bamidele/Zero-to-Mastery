#Error Handling

while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except ValueError as err:
        print(f'please enter a number : {err}')
    else:
        print('thank you')
        break