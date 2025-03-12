# MULTIPLE ARGS
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total

#print(multiply(1,3,5))




def add(x, y):
    return x + y

# add(*nums) utiliza el operador * para desempaquetar la lista nums. 
# Esto significa que los elementos de la lista se pasan como 
# argumentos separados a la función.
# En este caso, *nums se traduce en add(3, 5).
nums = [3, 5]
#print(add(*nums))

# Usando un diccionario
nums = {"x": 15, "y": 25}
#print(add(nums["x"], nums["y"]))

# Usando argumentos con nombre

#print(add(x=nums["x"], y=nums["y"]))

# Usando desempaquetado de diccionario
# En este caso, **nums utiliza el operador ** para desempaquetar 
# el diccionario nums como argumentos de la función.
# Esto es equivalente a add(x=15, y=25), donde las claves del diccionario 
# se utilizan como nombres de argumentos.
# El resultado será 40, que se imprime.

#print(add(**nums))

# ------------------------------------------------------------------
# NAMED ARGUMENT  AT THE END YOU MUST PASS A DEFINED ARGUMENT
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1,3,6,7,operator="*"))