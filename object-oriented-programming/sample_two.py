class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

action_figure = Toy('red', 10)
print(action_figure.__str__())