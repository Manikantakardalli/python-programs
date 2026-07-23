import random
import time

# ---------------- ROCK PAPER SCISSORS ----------------
def rock_paper_scissors():
    print("\n====== ROCK PAPER SCISSORS ======")

    options = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter rock, paper, or scissors: ").lower()

        if user not in options:
            print("Invalid Choice!")
            continue

        computer = random.choice(options)

        print("Computer:", computer)

        if user == computer:
            print("It's a Tie!")

        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("YOU WIN!")

        else:
            print("COMPUTER WINS!")

        play = input("\nPlay Again? (yes/no): ").lower()

        if play == "no":
            break


# ---------------- HANGMAN ----------------
def hangman():
    print("\n====== HANGMAN GAME ======")
    
    word = "freefire"
    guessed = ""
    chances = 5

    while chances > 0:
        display = ""

        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"

        print("\nWord : ",display)

        if display == word:
            print("YOU WIN")
            break
        
        guess = input("\nGuess a letter :")
        guessed += guess

        if guess not in word:
            chances -= 1
            print("\n WRONG GUESS")
            print("Chances left :",chances) 
    
    if chances == 0:
        print("\n YOU LOST")
        print("\nWORD WAS ",word)


# ---------------- GUESS THE NUMBER ----------------
def guess_number():
    print("\n====== GUESS THE NUMBER ======")

    number = random.randint(1,100)

    print("Guess the number (1 to 100) ")
    print("\nYou have 3 chances")

    for i in range(3):
        guess = int(input("Enter your guess : "))

        if guess == number:
            print("\nYOU WIN")
            break
        
        elif guess > number :
            print("\nToo High")

        else :
            print("\nToo Low")
    else:
        print("\nYOU LOST")
        print("NUMBER WAS ",number)



# ---------------- MEMORY GAME ----------------
def memory_game():
    print("\n====== NUMBER MEMORY GAME ======")
    score = 0

    while True:
        length = score + 3   # Number length increases with score

        number = ""

        for i in range(length):
            number += str(random.randint(0, 9))

        print("\nMemorize this number:")
        print(number)

        time.sleep(3)

        # Clear screen by printing blank lines
        print("\n" * 50)

        guess = input("Enter the number: ")

        if guess == number:
            score += 1
            print("Correct!")
            print("Score:", score)
        else:
            print("Wrong!")
            print("Correct number was:", number)
            print("Final Score:", score)
            break

        again = input("\nPlay next round? (y/n): ").lower()

        if again == "n":
            break



# ---------------- MAIN MENU ----------------
def main():

    while True:
        print("\n========== MINI GAMES ==========")
        print("1. Rock Paper Scissors")
        print("2. Hangman")
        print("3. Guess a Number")
        print("4. Number Memory Game")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            rock_paper_scissors()

        elif choice == "2":
            hangman()

        elif choice == "3":
            guess_number()

        elif choice == "4":
            memory_game()

        elif choice == "5":
            print("\nThanks for Playing ")
            break

        else:
            print("Invalid Choice!")


# ---------------- START PROGRAM ----------------
main()
    
     
    
