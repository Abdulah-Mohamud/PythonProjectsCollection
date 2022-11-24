#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? £" ))
tip = int(input("What percentage tip would you like to pay? "))
people = int(input("How many people will split the bill? "))

total_bill = bill * (1 + (tip/100))
bill_per_person = "{:.2f}".format(total_bill/people, 2)

print(f"The bill per person is £{bill_per_person}")