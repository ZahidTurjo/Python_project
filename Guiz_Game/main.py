from quiz_database import question_bank
from quiz_database import options
print("**************")
print("Welcome to my quiz game")


score=0
total=0
for question_num in range(len(question_bank)):
    print("*********")
    
    print(question_bank[question_num]['text'])
    for i in options[question_num]:
        print(i)
    
    guess=input("Enter your answer(A/B/C/D): ").upper()
    if guess == question_bank[question_num]['answer']:
        print("Your answer is correct")
        score+=1
        total+=1
        print(f"your score is {score}/{total}")
    else:
        print("Your answer is wrong")
        total+=1
        print(f"your score is {score}/{total}")
percentage=(score/total)*100 
print(f"your total correct answer percnetages is {percentage} %")    
            
         
       