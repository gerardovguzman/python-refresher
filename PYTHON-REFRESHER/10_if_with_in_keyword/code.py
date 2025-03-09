

number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input == 'y':
    while True:  # Bucle para permitir múltiples intentos
        user_input = int(input("Guess the number: "))
        
        if user_input == number:
            print(f"You've guessed the number! The number is {number}")
            another_try = input("Would you like to try again? (y/n)?: ")
            if another_try == 'y':
                continue  # Reinicia el bucle para jugar de nuevo
            else:
                print("Thanks for playing.")
                break  # Sale del bucle
        else:
            print("Wrong number")
            if number - user_input in (1,-1):
                print("You were off by one.")
            elif abs(number - user_input) == 2:
                print("You were off by two.")
            another_try = input("Would you like to try again? (y/n)?: ")
            if another_try != 'y':
                print("Thanks for playing.")
                break  # Sale del bucle
else: 
    print("No problem. I'll be here when you want to.")
