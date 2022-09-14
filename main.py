from random import randint

lives = 0

number = randint(1, 100)


def check_answer(guess):
    if guess != number:
        return lives - 1
    else:
        return lives - lives


def change_difficulty(difficulty):
    if difficulty == "easy":
        return lives + 10
    elif difficulty == "hard":
        return lives + 5


print("""
 _____                       _   _            _   _                 _               
|  __ \                     | | | |          | \ | |               | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|                                                                                    
""")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answers = ["easy", "hard"]
answer = None
while answer not in answers:
    answer = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = change_difficulty(answer)

while lives != 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    while True:
        try:
            guess = int(input("Make a guess: "))
            break
        except ValueError:
            print("Please only guess a whole number")
            continue
    lives = check_answer(guess)
    if guess > number:
        print("Too high.")
        if lives != 0:
            print("Guess again.")
    elif guess < number:
        print("Too low.")
        if lives != 0:
            print("Guess again.")

if guess == number:
    print(f"Congratulations! You won! The number I was thinking of: {number}")
elif guess != number:
    print(f"I'm sorry, you lost. The number I was thinking of: {number}")
