'''this project creates a simple game structure of guessing the number that the opponent 
has in mind. the game gives 5 lives to the guesser, and takes the life value 1 value 
down while calculating how many guesses it takes the guesser to find the number.
'''

import random
number = random.randint(1, 50)
lives = 5
count = 0
print('Guess a number between 1-50. You have 5 chances!')
while lives > 0:
    lives -= 1
    count += 1
    guess = (int(input(f'{count}. guess: ')))

    if guess == number:
        print(f'Correct at {count}. guess! You receive {100 - 20*(count-1)} points.')
        break
    elif guess < number:
        print('higher')
    else:
        print('lower')
        
    if lives == 0:
        print(f'You are out of guesses! The correct number is {number}. You receive 0 points.')
