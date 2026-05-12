print("welcome to the treasure island \n your mission is to find the treasure \n you are at the cross of the road")
side = input("type Left or Right :")
if side == "Left":
    
    print("you enter near the pond ")
    swim_wait = input("enter swim or wait : ")
    if swim_wait == "Wait":
        print("reach door")
        door = input("which door Red, Blue, Yellow: ")
        if door == "Red":
            print("burned by fire . Game Over")
        elif door == "Blue":
            print("Eaten by beasts. Game Over")
        elif door == "Yellow":
            print("you win!")
        else :
            print("Game Over")
    elif swim_wait == "Swim":
        print("Attacked by trout")
    else:
        print("Game over")
elif side == "Right":
    print("fall into a hole Game Over")
else:
    print("game over")