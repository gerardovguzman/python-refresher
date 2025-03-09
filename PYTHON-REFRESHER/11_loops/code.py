# WHILE LOOP
'''
number = 7

while True:
    user_input = input("Would you like to play? (Y/n): ")
    if user_input == 'n':
        break

    user_input = int(input("Guess the number: "))    
    if user_input == number:
        print(f"You've guessed the number! The number is {number}")
    elif abs(number - user_input) == 1:
        print("You were off by one.")
    else:
        print("Sorry. Wrong number")
'''


# FOR LOOP
friends = ["Rolf","Jen","Bob","Anne"]

#for friend in friends:
#    print(f"{friend} is my friend.")

#for friend in range(4):
#   print(f"{friend} is my friend")

grades = [35,67,98,100,100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)