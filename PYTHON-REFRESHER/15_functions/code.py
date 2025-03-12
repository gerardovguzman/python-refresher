def hello(a):
    print(f"hello {a}")
#hello("Gera")


def user_age_in_seconds():
    user_age = int(input("Enter yoour age: "))
    print("**** loading ****")
    age_seconds = user_age * 365 * 24 *60 
    print(f"Your age, {user_age}, in seconds, is: {age_seconds}")

#print("Welcome to the age seconds calculator!")
#print("--------------------------------------")
#user_age_in_seconds()
#print("Thanks for playing!")


friends = ["Rolf","Bob"]
'''
def add_friend():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name]
    print(f)

#add_friend()
'''

# THIS COULD SEEMS CONFUSING, BUT IT IS VALID CODE

def add_friend():
    friends.append("Rolf")

friends = []
add_friend()

print(friends)  # Rolf


