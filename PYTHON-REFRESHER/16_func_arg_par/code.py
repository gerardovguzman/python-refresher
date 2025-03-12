def add(x,y):  # x & y are parameters
    result = x + y 
    print(result)

add(5,3)   # 5 & 3 are arguments


def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Guzman",name="Gera")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("Division by zero is not an allowed operation")
    
divide(4,3)