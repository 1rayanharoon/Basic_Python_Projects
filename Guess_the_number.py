import random

def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter a number between 1 and 10: "))
        if guess>random_number:
            print("Sorry guess again. Too high")
        elif guess<random_number:
            print("Sorry try again. Too low")

    print(f"Congrats You guessed the correct number {random_number}")



def computer_guess(x):
    feedback=""
    low=1
    high=x
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"The number {guess} you guessed is correct")


computer_guess(1000)

            
