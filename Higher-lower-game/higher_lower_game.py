import random
import os
import game_artr
import game_database
print(game_artr.game_logo)
score=0

def display_account_info(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name} ,a {description}, from {country} "

def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess ==1:
            return False
        else:
            return True
    else:
        if guess ==1:
            return True
        else:
            return False
account2=random.choice(game_database.data)
print(f"sajdhjasdh{account2}")
end_process=False
while not end_process:
    if score !=0:
        print(f'You are right.Now your score is {score}')
    account1= account2
    account2=random.choice(game_database.data)
    while account1 == account2:
         account2=random.choice(game_database.data)

    print(f"Compare 1:{display_account_info(account1)}")
    print(game_artr.vs  )
    print(f"Compare 2:{display_account_info(account2)}")
    guess=int(input('Which one have more followers 1 or 2 :'))
    followers_count1=account1['followers_count']
    followers_count2=account2['followers_count']
    is_correct=check_answer(guess,followers_count1,followers_count2)

    if is_correct:
        score+=1   
        os.system('cls')
    else:
        print(f"You are worng.Your final score is {score}")
        end_process=True



