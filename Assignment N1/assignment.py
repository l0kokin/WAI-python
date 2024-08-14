import random

print('Welcome to the Simple Multiplication Quiz! You will be given 5 multiplication problems to solve.')

numProblems = 1
score = 0

while  numProblems <= 5:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    print(f'Problem 1: What is {num1} X {num2}')

    user_input = float(input('Your Answer: '))

    if user_input == answer:
        print('Correct!')
        score += 1
    else: 
        print(f'Incorrect. the correct answer was {answer}.')
    
    numProblems += 1

print(f'You scored {score} out of {numProblems}. Well done!')
