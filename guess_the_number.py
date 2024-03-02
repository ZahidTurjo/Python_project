import random
ATTEMPTS_EASY=10
ATTEMPTS_HARD=5

def set_level_difficulty(level):
    if level == 'easy':
        return ATTEMPTS_EASY
    elif level == 'hard':
        return ATTEMPTS_HARD
    else:
        return
    
def check_answer(guess_number,answer,attempts):
    if guess_number <answer  :
        print("Your guess is too low")
        print('Guess again')
        return attempts-1
    elif guess_number>answer:
        print("Your guess is too high")
        print('Guess again')
        return attempts-1
    else:
        print(f'Your answer is right .. the answer was {answer}') 

def game():
    print('let me think about a number between 1 to 50')
    answer= random.randint(1,50)
    print(answer)
    print("Guess the number--->")   
    level=input("Choose the level type 'easy' or 'hard' :")
    attempts= set_level_difficulty(level)
    if attempts!= ATTEMPTS_EASY and attempts != ATTEMPTS_HARD:
        print("u entered a worng level.... play again")
        return

    guessing_number =0
    while guessing_number !=answer and attempts>0:
        print(f"you have {attempts} attempts remaining")
        guessing_number=int(input('Guess the number: '))
        attempts=check_answer(guessing_number,answer,attempts) 
        if attempts ==0:
            print('u are lose al the attemps')
            return

    
game()


