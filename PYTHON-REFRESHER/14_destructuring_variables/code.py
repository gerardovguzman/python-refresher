'''
Destructuring (also called unpacking) is where we take a collection, 
like a list or a tuple, and we break it up into individual values. 
This allows us to do things like destructuring assignments, where 
we assign values to several variables at once from a single collection.
'''

# given 
x = 5,11
# we can separate this into 2 variables
x, y = 5,11

# estamos desestructurando la variable, en 2 variables
t = 5,11
x, y = t
print(x,y)

# printing the dictionary as a for loop
student_attendance = {"Rolf":94,"Bob":80,"Anne":100}

for st, at in student_attendance.items():
    print(f"{st}: {at}")


# priting this as a list, we'll have a list of tuples
#print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)


# INSTEAD OF A DICTIONARY, WE HAVE HERE A LIST OF TUPLES WITH 3 VALUES EACH
# WE MUST HAVE ALL THE THREE VALUES IN EACH TUPLE
people = [("Bob",42,"Mechanic"),("James",24,"Artist"),("Harry",32,"Lecturer")]

for name, age, profession in people:
    print(f"name:",{name},", age:",{age},", profession:",{profession})

# WE CAN GET DIFFERENT VALUES FOR DIFFERENT PERSONS
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

# EXTRACT SOME VRAIABLES, BUT NOT ALL OF THEM
person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)


head, *tail = [1,2,3,4,5]
print(head)
print(tail)

*head, tail = [1,2,3,4,5]
print(head)
print(tail)