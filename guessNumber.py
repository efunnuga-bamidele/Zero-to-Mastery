from random import randint

def runGuess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1 ~ 10')
        return False

answer = randint(1, 10)

if __name__ == "__main__":
    while True:
        try:
            guess = int(input('Guess a number 1 ~ 10: '))
            if(runGuess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue


