# REGULAR FUNCTION
#def add(x,y):
#    return x + y

#print(add(5,7))

# REWRITE AS A LAMBDA FUNCTION
# we can give this function a name, like below
add = lambda x, y: x + y
#print(add(5,6))

# otherwise, we can write the function this way
#print((lambda x, y: x + y)(5,7))

# 
def double(x):
    return x * 2

sequence = [1,3,5,9]
# instead of writing this...
doubled = [x * 2 for x in sequence]
#print(doubled)
#... we can call the function in there
doubled = [double(x) for x in sequence]
#print(doubled)

# USING THE MAP FUNCTION, WHERE THE LAMBDA MAKES MORE SENSE
# we don't need the function definition above
# def double(x):
#    return x * 2
sequence = [2,4,6,8]
#doubled = [(lambda x: x * 2)(x) for x in sequence]
# map function will return an objetc, so in order to print out 
# the result of the function, we need to convert the function as a list
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)

# LAMBDA ARE FUNCTIONS WITHOUT A NAME
# TO GIVE THEM A NAME, WE NEED TO ASSIGN THEM TO A VARIABLE
# SE USAN PARA DEVOLVER UN VALOR A PARTIR DE SUS PARÁMETROS

