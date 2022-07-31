import datetime
print("This is a simple \"Guess Your Age Application\"! ")

birth_year = int(input("What year where you born? "))

def guessYourAge(age):

    your_age = datetime.datetime.now().year - age
    return f"You are {your_age} years old!"


print(guessYourAge(birth_year))