import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option 1 in random
random_friends = random.choice(friends)
print(random_friends)

#random in a list of chaoices 
random_name  = random.randint(0,4)
print(friends[random_name])
