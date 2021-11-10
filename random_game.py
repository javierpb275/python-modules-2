from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

first_number = int(sys.argv[1])
last_number = int(sys.argv[2])

while True:
    try:
        guess = int(input(f'guess a number {first_number}~{last_number}:  '))
        if first_number <= guess <= last_number:
            if guess == answer:
                print('that is correct!')
                break
        else:
            print(f'I said {first_number}~{last_number}')
    except ValueError:
        print('please enter a number')
        continue