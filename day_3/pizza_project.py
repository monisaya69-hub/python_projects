print("welcome to python piza delivery")
piza_size = input("enter the Size of the Pizza you want , S for small, M for medium , and L for Large : ")

P_S = piza_size[0].upper()
bill = 0 

if P_S == "S":
    bill = 15
    print(f"your price for the small pizza was: £{bill}")
    peproni = input("Add Pepporoni for small pizza (Y or N):")
    if peproni.upper() == "Y":
        bill += 2
        print(f"prize for the piza with pepporoni was: £{bill}")
elif P_S =="M":
    bill = 20
    print(f"your price for the medium pizza was : £{bill}")
    peproni = input("Add Pepporoni for Medium pizza (Y or N):")
    if peproni.upper() == "Y":
        bill += 3
        print(f"prize for the piza with pepporoni was: £{bill}")
elif P_S == "L":
    bill = 25
    print(f"your price for large pizza was : £{bill}")
    peproni = input("Add Pepporoni for Large pizza (Y or N):")
    if peproni.upper() == "Y":
        bill += 3
        print(f"prize for the piza with pepporoni was: £{bill}")
chese = input("add an extra chese for any pizza Y or N :")
if chese.upper() == "Y":
    bill += 2
    print(f"your total bill , for the piza was :£{bill}")

else :
    print("you enter a wrong size of the pizza")


