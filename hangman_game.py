import random

print("welcome to HangmanGame")
word_list=["apple", "banana", "orange", "grape",
            "strawberry", "watermelon", "pineapple", 
             "mango", "pear"]
hangman_stages = [
    
    """
     _______
    |       |
    |       O
    |
    |
    |
    |
    |________
    """,
    """
     _______
    |       |
    |       O
    |       |
    |
    |
    |
    |________
    """,
    """
     _______
    |       |
    |       O
    |      /|
    |
    |
    |
    |________
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |
    |
    |
    |________
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      /
    |
    |
    |________
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    |
    |________
    """
]
 
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]

for i in range(len(chosen_word)):
    display +='_'
print(display)  

lives=6
length=len(chosen_word)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guessed_letter:
            display[position]=letter
            # length-=1
            # if length==0:
            #     game_over=True
            #     print("You won")

    print(display)
    if guessed_letter not in chosen_word:
        print(hangman_stages[-lives])
        lives-=1  
            
        if lives==0:
            game_over=True
            print('Game Over')
    if '_' not in display:
        game_over=True
        print("You won")
        