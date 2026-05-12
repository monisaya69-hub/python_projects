import random
# we can use diffenerent random functions . random(), randint(), uniform()
# rand_num = random.randint( 4, 33)

# print(rand_num)
# ok lets build a program for heads and tails ,  using the random function
rand_num = random.randint(0,1)
if rand_num == 0:
    print("heads")
else: 
    print("tails")