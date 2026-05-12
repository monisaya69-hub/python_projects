import random
friends = ["chakravarthi" , "mahesh", "banti", "vasthav", "sandeep", "srikanth"]

#1 way
print(random.choice(friends))

#2nd way
x= random.randint(0, 5)

print(friends[x])