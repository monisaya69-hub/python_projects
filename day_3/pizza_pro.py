print("welcome to the pizza delivery")
size =  input("enter the size of the piza you want S,M or L:")
pepproni = input("do you like to add pepporoni Y or N :")
chese = input ("do you like to add extra chese Y or N:")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill +=20
elif size == "L":
    bill +=25
else:
    print("you enter the wrong size of the piza")

if pepproni == "Y":
    if size == "S":
        bill +=2
    else:
        bill += 3
if chese == "Y":
    bill +=2 


print(f"your final bill was : £{bill}")

