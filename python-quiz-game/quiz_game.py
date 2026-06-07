print('*** QUIZ GAME ***')
play=input('do you want to play this game?')
if play.lower()=='no':
    quit()
print("Let's play the game :) !!!")
score=0

answer=input('1. What is the capital of Japan?')
if answer.lower()=='tokyo':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('2. Which planet is known as the Red Planet?')
if answer.lower()=='mars':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('3. Who wrote the play Romeo and Juliet?')
if answer.lower()=='william shakespeare':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('4. What is the largest ocean on Earth?')
if answer.lower()=='pacific ocean':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('5. How many continents are there on Earth?')
if answer.lower()=='7':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('6. What is the chemical symbol for gold?')
if answer.lower()=='au':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('7. Which country is famous for the pyramids of Giza?')
if answer.lower()=='egypt':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('8. Who developed the theory of relativity?')
if answer.lower()=='albert einstein':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('9. What is the largest mammal in the world?')
if answer.lower()=='blue whale':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

answer=input('10. Which gas do plants primarily absorb from the atmosphere for photosynthesis?')
if answer.lower()=='carbon dioxide':
    print("Correct !!!")
    score+=1
else:
    print('Incorrect !')

print(f'Total Score = {score}/10')
print(f'YOU GOT {(score/10)*100}% CORRECT !!!')