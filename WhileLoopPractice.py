# Ashton Wood
# 03-31-2023
# While Loop Practice
# A while loop increments 1 to 7

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print(number, 'is too low')
    elif number == guess_me:
        print('Correct')
        break
    else:
        print('you broke it')
        break
    number += 1

