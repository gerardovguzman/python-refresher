# DEFAULT VALUES
# default parameteres must be at the end
def add(x,y=8):
    print(x+y)

add(5,7)

default_y = 3

def add_1(x,y=default_y):
    print(x+y)

add_1(7,2)

