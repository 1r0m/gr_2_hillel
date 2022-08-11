import random

number = random.randint(1, 10)
print ("Я загадав число від 1 до 10.")
print("В тебе є 3 спроби.")

guesses_made = 0

while guesses_made < 3:  
    guess = int(input('Введи число: '))

    guesses_made += 1

    if guess < number:
        print ("Ваше число менше загаданого")

    if guess > number:
        print ("Ваше число більше загаданого")

    if guess == number:
        break

if guess == number:
    print ("You won!")
else:
    print ("You lose")
   