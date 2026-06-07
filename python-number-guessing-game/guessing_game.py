import random
def get_range():
    max_number=input('enter top range of the number(greater than 10):')
    if max_number.isdigit() and int(max_number)>10:
        return max_number
    else:
        print('Enter a number greater than 10')
        return get_range()

max_number=int(get_range())

def get_guess():
    guessed_num=input('Guess a number:')
    if guessed_num.isdigit():
        return guessed_num
    else:
        print('Enter a valid number.')
        return get_guess()



random_number=random.randint(11,max_number)
print()

if max_number<31:
    no_of_attempts=5
elif  max_number<71:
    no_of_attempts=7
else:
    no_of_attempts=10

print(f'You have {no_of_attempts} attempts in total.')
print()

for i in range(1,no_of_attempts+1):

    guessed_num = int(get_guess())

    if guessed_num==random_number:
        print('U GUESSED IT RIGHT !!!')
        print(f'You guessed it in {i} attempts.')
        break
    elif guessed_num>max_number:
        print(f'enter a number less than {max_number}')
    elif guessed_num>random_number:
        print("WRONG! Your number is higher than the number.")
    else:
        print('WRONG! Your number is lower than the number.')
    attempts_left=no_of_attempts-i
    print(f"Number of attempts left: {attempts_left} ")
    print()
else:
    print("Out of attempts !!, Better luck next time.")
    print(f'The number is : {random_number}')