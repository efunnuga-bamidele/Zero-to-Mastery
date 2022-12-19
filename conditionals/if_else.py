is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')
# elif is_licenced:
#     print('you can drive now!')
else:
    print('you are not of age!')

print('okoko')

# Ternary Operator / Conditional Expression
is_friend = False
can_message = "Message allowed" if is_friend else "Not allowed to message"

print(can_message)


# Short Circuiting
is_User = True

if is_friend or is_User:
    print('best friends forever')