#OOP
# 4 Pillars of OOP
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

class PlayerCharacter:
    #Class Object Attribute
    membership = True
    def __init__(self, name='annymous', age=0):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name} and i am {self.age} years old.')

player1 = PlayerCharacter('Tom', 10)
player1.shout()


# Example 2 for inheritance

class User:
    # Parent Class
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User): # inherit User Class Function
    # Children Class
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User): # inherit User Class Function
    # Children Class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50, 'merlin@mail.com')
archer1 = Archer('Robin', 100)
# wizard1.attack()
# archer1.attack()
print(wizard1.email)

# print(isinstance(wizard1, User))

# Polymorphism
# for move in [wizard1, archer1]:
#     move.attack()