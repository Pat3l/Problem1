import random

print("Enter the value of number in between you want to start a game.")
num1 = int(input("Enter the first number:\n "))
num2 = int(input("Enter the second number:\n "))

randomNumber1 = random.randint(num1, num2)
randomNumber2 = random.randint(num1, num2)

print("Player1 Turn: \n")
player1guess = None
guessesofP1 = 0

while randomNumber1 != player1guess:
    player1guess = int(
        input(f"Guess the number between {num1} and {num2}, Player1: \n"))
    guessesofP1 += 1

    if num1 <= player1guess <= num2:
        if randomNumber1 == player1guess:
            print("Player1: Congratulation!! you guessed the right number.")

        else:
            if randomNumber1 < player1guess:
                print("You guessed wrong number, guess smaller number.")

            elif randomNumber1 > player1guess:
                print("You guessed wrong number, guess bigger number.")

    else:
        print(f"Your guess should be a number between {num1} to {num2}.")

print(f"Player1, You guessed the number in {guessesofP1} guesses.")


print("Player2 Turn: \n")
player2guess = None
guessesofP2 = 0

while randomNumber2 != player2guess:
    player2guess = int(
        input(f"Guess the number between {num1} and {num2}, Player2: \n"))
    guessesofP2 += 1

    if num1 <= player2guess <= num2:
        if randomNumber2 == player2guess:
            print("Player2: Congratulation!! you guessed the right number.")

        else:
            if randomNumber2 < player2guess:
                print("You guessed wrong number, guess smaller number.")

            elif randomNumber2 > player2guess:
                print("You guessed wrong number, guess bigger number.")

    else:
        print(f"Your guess should be a number between {num1} to {num2}.")

print(f"Player2, You guessed the number in {guessesofP2} guesses.")


if guessesofP1 < guessesofP2:
    print("Player1 wins the game.")

elif guessesofP1 > guessesofP2:
    print("Player2 wins the game.")

elif guessesofP1 == guessesofP2:
    print("This game is a Tie.")

print("Thanks for playing.")
