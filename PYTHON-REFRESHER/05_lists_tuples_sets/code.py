# LIST
 # list, square brackets
print("------- LIST -------")
l = ["Bob","Rolf","Anne"]  
print(l[1])
# I can modified a value
l[0] = "Gera"
# add elements at the end of the list
l.append("Erika")
l.remove("Rolf")
print(l)

# TUPLE
# tuple, you cannot modifie a tuple
print("------- TUPLE -------")
t = ("Bob","Rolf","Anne")  
print(t[0])
# I cannot maka changes on tuples
#t[0] = "Gera"
#print(t)  this will through an error

# SET
# set, curly braces.. you may modifie, but you cannot duplicate an element
# there is no an order specified of the indexes
print("------- SET -------")
s = {"Bob","Rolf","Anne"}  
# for adding
s.add("Erika")
s.remove("Anne")
print(s)