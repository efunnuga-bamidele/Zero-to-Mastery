import datetime
print("This is a simple \"Guess Your Age Application\"! ")

birth_year = int(input("What year where you born? "))

def guessMyAge(birth_year):

    my_age = datetime.datetime.now().year - birth_year
    print(f"You are currently {my_age} years old!")
19
guessMyAge(birth_year)