# #range function 
# c = 0
# for i in range(1, 101):
#     c += i
# print(c)

print("welcome to the game FizzBuzz")

for number in range(1, 101):
    
    if number%3 == 0 and number%5 == 0 :
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)