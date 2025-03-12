# GIVEN A LIST OF USERS WITH 4 TUPLES INSIDE

users = [
    (0,"Bob","password"),
    (1,"Rolf","bob123"),
    (2,"Jose","longp4assword"),
    (3,"username","1234"),
]

# we get the user name user[1], associate that with the tuple
# wich is the element called user in the list
# inside of the list users
username_mapping = {user[1]: user for user in users}
print(username_mapping)

# IF I KNOW THE NAME OF THE USER
print(username_mapping["Jose"])

# EXAMPLE FOR LOGIN
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct")
else:
    print("Try again")

'''
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
Aquí, se están solicitando al usuario dos entradas:
username_input: el nombre de usuario que el usuario ingresa.
password_input: la contraseña que el usuario ingresa.
Ambas entradas se almacenan como cadenas en las variables correspondientes.

-----------------------
_, username, password = username_mapping[username_input]
Aquí se utiliza el diccionario username_mapping (que se creó en el código anterior) para obtener la tupla correspondiente al username_input.
username_mapping[username_input] busca la tupla asociada al nombre de usuario ingresado.
Luego, la tupla se descompone en tres variables utilizando la sintaxis de desestructuración:
_: se usa para ignorar el primer elemento de la tupla (el ID), ya que no es necesario en este contexto.
username: se asigna el nombre de usuario (que es redundante aquí, ya que ya lo tenemos en username_input).
password: se asigna la contraseña de la tupla.

--------------------
if password_input == password:
    print("Your details are correct")
else:
    print("Try again")
Se compara la entrada de contraseña del usuario (password_input) con la contraseña obtenida de la tupla (password).
Si las contraseñas coinciden, se imprime "Your details are correct".
Si no coinciden, se imprime "Try again".

'''
