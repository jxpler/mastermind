import random
from time import sleep


print("=" * 10 + "Mastermind" + "=" * 10)
name = input("Enter your name: ")
if name == '':
    name = "Player"

welcomemsg = (f"Welcome, {name}! \n" +
              f"The rules are simple.\nI am thinking of a number and your goal is to guess that "
              "number.\nYour score will be displayed at the end of the game.\n"
              "If you wish to quit the game type 'Exit'\n\n"
              "The number I am thinking of is...\n")

for char in welcomemsg:
    sleep(0.075)
    print(char, end='', flush=True)


def num_guess():
    return input("What is your guess?: ")


def end_screen():
    print("=" * 40 + "\n")
    print(f"    Total guesses: {total_guesses}\n"
          f"    Correct guesses: {total_guesses_corect}\n"
          f"    Incorrect guesses: {total_guesses_incorrect}\n")
    print("=" * 40)


def end_screenp(guess_p):
    print("=" * 40 + "\n")
    print(f"    Total guesses: {total_guesses}\n"
          f"    Correct guesses: {total_guesses_corect}\n"
          f"    Incorrect guesses: {total_guesses_incorrect}\n"
          f"    Correct guess percentage: {guess_p}%\n")
    print("=" * 40)


total_guesses = 0
total_guesses_corect = 0
total_guesses_incorrect = 0

answer = random.randint(0, 10)

while True:
    guess = num_guess()
    guess.strip()

    if guess.lower() == 'exit' and total_guesses > 0:
        guess_p = total_guesses_corect / total_guesses * 100
        end_screenp(guess_p)
        break
    elif guess.lower() == 'exit' and total_guesses == 0:
        end_screen()
        break

    if guess == '':
        print("You have to enter a number! Try again!\n")
        continue

    try:
        guess = int(guess)
        if guess >= 11:
            print("Number is outside the range!\n")

        elif guess != answer:
            print("Incorrect! Keep guessing!\n")
            total_guesses_incorrect += 1
            total_guesses += 1

        elif guess == answer:
            print("You guessed correctly!\n")
            total_guesses_corect += 1
            total_guesses += 1
            play_again = str(input("Would you like to play again? (Y/N): ")).strip().lower()
            while play_again not in ["y", "n"]:
                print("Invalid input, try again!\n")
                play_again = str(input("Would you like to play again? (Y/N): ")).strip().lower()

                if play_again == "y":
                    answer = random.randint(0, 10)
                    print("\nThe new number I am thinking of this time is...")
                    continue

                elif play_again == "n":
                    guess_p = total_guesses_corect / total_guesses * 100
                    end_screenp((round(guess_p, 2)))
                    break

    except ValueError:
        print("Invalid input, try again!\n")
