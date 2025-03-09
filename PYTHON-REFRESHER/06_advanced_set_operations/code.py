friends = {"Bob","Rolf","Anne","Gera","Erika"}
abroad = {"Bob","Anne","Erika"}
#print(friends)
#print(abroad)

# for calculating who is abroad and who is not
local_friends = friends.difference(abroad)
#print(local_friends)

local_friends = abroad.difference(friends)
#print(local_friends)

art = {"Draw", "Music","Biology"}
science = {"Chemicks","Biology"}

subjetcs = art.union(science)
print(subjetcs)

both = art.intersection(science)
print(both)