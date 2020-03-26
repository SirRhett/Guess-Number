from random import randint

num = randint(1,100)

print('The rules for this game are very simple.\nAll you have to do is put in guesses for your number and the program will tell you if you are closer or farther away from the number.')
print('You can not choose a number that is less than 1 or greater than 100')
print('If your guess is within 10 of the number i will tell you WARM and if not then COLD')
print('If you get closer ill tell you WARMER and if you move away then COLDER')

guesses = [0]

while True:
    
    guess = int(input('Enter your guess here: '))

    if guess > 100 or guess < 1:
        print(int(input('OUT OF BOUNDS, Try again: ')))   
        continue
    
    if guess == num:
        print(f'CONGRATS YOU GUESSED IT IN {len(guesses)} GUESSES!')
        break
    
    guesses.append(guess)
              
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
               
pass