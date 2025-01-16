import random
def guessing_Game():
    print("Welcome to the Guessing Game")
    print("Guess the number between 0 to 10")
    print("-" * 30)

    random_num = random.randint(0,10)
    attempt = 0
    attempt_max = 5

    while attempt < attempt_max:
        try:
            guessing_number = int(input("Enter the guess: "))

            if guessing_number < 0 or guessing_number > 10:
                print("Please enter valid number between 0 to 10")
                continue

            attempt += 1
    
            if random_num == guessing_number:
                print(f"Congratulation ! You guessed it right in {attempt} attempt")
                break
            elif guessing_number < random_num: 
                print("Too low! , Try again")
            else: 
                print("Too high! , Try again")
            print("Attempt left: ", attempt_max - attempt)
    
        except ValueError: 
            print("Invalid input. Please enter a number: ")
    else:
        print("Game Over , You have used all attempts")
        print(f"The number was {random_num}")
    
    play_again = input("Do you want to play again (yes/no)!:").lower().strip()
    if play_again == 'yes':
        guessing_number()
    else:
        print("Thanks for playing! Good Bye")
    
guessing_Game()