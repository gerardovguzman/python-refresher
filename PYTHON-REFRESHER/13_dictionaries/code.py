friend_ages = {"Rolf": 24,"Adam":30,"Anne":27}
'''
print(friend_ages)
print(type(friend_ages))
print(len(friend_ages))
print(friend_ages.keys())
print(friend_ages.values())'
'''

# accessing a particular element
# index won't work on dictioaries, we must access through the key
#print(friend_ages["Adam"])

# for adding
#friend_ages["Bob"] = 30

#print(friend_ages)


# WE CAN HAVE A LIST OF DICIONTARIES
friends = [
    {"name": "Rolf","age": 24},
    {"name": "Adam","age": 30},
    {"name": "Anne","age": 27}
]
#print(friends)

# for a particular friend, this is a list so we can 
# look for through index
#print(friends[0])
#print(friends[1]["name"])




student_attendance = {"Rolf":96,"Bob":80,"Ane":100}

# ITERATE A DICTIONARY OVER A FOR LOOP
# the following could be, but...
'''
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")
'''
#... there is a better way
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
'''
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance["Bob"]}")
else:
    print("Bob is not a student")'
'''

# IF I WANT JUST THE VALUES, AND ITS AVERAGES
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))