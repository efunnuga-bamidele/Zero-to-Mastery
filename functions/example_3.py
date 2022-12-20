# Scope - what variables do i have access to?

a = 1

def confunsion():
    a = 5
    return a


print(confunsion())

print(a)


total = 0
def count():
    global total
    total += 1

    return total

count()
count()
print(count())

