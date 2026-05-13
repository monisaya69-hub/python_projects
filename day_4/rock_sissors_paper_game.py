import random
# rock
# scissors
# paper

user_enter= int(input("enter a number to play 0 for rock, 1 for scissors and 2 for paper: "))

computer_pick = random.randint(0, 2)

if user_enter >= 3 :
    print("you entered a invalid number, game over computer wins")
elif (user_enter == 0 and computer_pick == 2)or(user_enter == 2 and computer_pick == 1)or(user_enter==1 and computer_pick == 0):
    print("you lose, comp win")
elif user_enter == computer_pick:
    print("game draw")
elif (user_enter == 1 and computer_pick == 2) or (user_enter == 2 and computer_pick == 0)or(user_enter == 0 and computer_pick == 1):
    print("you win, comp lose")
