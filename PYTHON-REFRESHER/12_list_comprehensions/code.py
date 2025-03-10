numbers = [1,2,3]
double = []

'''
for number in numbers:
    double.append(number * 2)
print(double)
'''

# In a list comprehension, we could do this way
numbers = [1,2,3]
double = [n * 2 for n in numbers]
#print(double)

friends = ["Rolf","Sam","Samantha","Sebastian","Jen"]
starts_s = []
'''
for f in friends:
    if f.startswith("S"):
        starts_s.append(f)
print(starts_s)
'''

friends = ["Rolf","Sam","Samantha","Sebastian","Jen"]
starts_s = [f for f in friends if f.startswith("S")]

'''
if we remove the others names of the friends list
they won't be the same list anyway because
they're using differente spaces of memory
'''

friends = ["Sam","Samantha","Sebastian"]

print(friends)
print(starts_s)
print(friends is starts_s)

# using id we can see the different spaces in memory ADDRESS MEMORY
print("friends:",id(friends),"starts_s:",id(starts_s))

