
def highest_even(li):
    # number = 0
    # for num in li:
    #     if num % 2 == 0 and num > number:
    #         number = num
    # return number
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11, 14]))