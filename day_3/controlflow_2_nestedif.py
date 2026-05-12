print("welcome to the rolercoster")

height = int(input("please enter your height"))

if height > 120 :
    print("you can ride the rolarcoster")
    age = int(input("plese enter your age"))
    if age <= 10:
        print("your ticket price was 12£")
    elif age < 18:
        print("your ticket price was 15£")
    else :
        print("your ticket price was 20")
else:
    print("you have to grow heigh enough to ride the rolarcoster")
    