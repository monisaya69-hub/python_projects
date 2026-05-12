print("welcome to the rolercoster")

height = int(input("please enter your height"))
bill = 0
if height > 120 :
    print("you can ride the rolarcoster")
    age = int(input("plese enter your age"))
    if age <= 10:
        bill = 12
        print("your ticket price was 12£")
    elif age < 18:
        bill = 15
        print("your ticket price was 15£")
    else :
        bill = 20
        print("your ticket price was 20")
    photo = input("if you need a photo enter y for yes or n for no")
    if photo == "y":
        bill += 3
    print(f"your total bill was : {bill}")
else:
    print("you have to grow heigh enough to ride the rolarcoster")
    