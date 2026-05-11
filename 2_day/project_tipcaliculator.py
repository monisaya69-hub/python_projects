print("click the run the final project to build a tip calculator that calculates the tip amount based on the bill amount and the tip percentage")
print("welcome to the tip calculator!" )
bill_amount = int(input("what is the total bill amount? "))
tip_amount_percent = int(input("how much tip would you like to give? 10, 12, or 15? "))
no_people = int(input("how many people to split the bill into? "))
tip_amount= (tip_amount_percent/100)*bill_amount
total_bill_per_person = round((bill_amount + tip_amount)/no_people,2)
print(f"each person should pay $ {total_bill_per_person}")