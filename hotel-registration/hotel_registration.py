#=========================================
# CREATED BY: GUILHERME ARO
# DATE: 03/26/2026
# Holiday Colony Program
#=========================================

# Holiday Colony - Hotel
# Inputs - Name, type of apartment, number of people, days staying
while True:
    name = input("Hello, welcome to the UMC hotel! How would you like to be called? ")
    if not name.replace(" ", "").isalpha():
        print("Fill this field only with letters")
        continue
    break

while True:
    try:
        type_APTO = int(input("Which type of apartment did you prefer? (1 or 2) "))
    except ValueError:
        print("Please type a valid number!")
        continue
    if type_APTO < 1 or type_APTO > 2:
        print("We only have the options 1 and 2")
        continue
    break

while True:
    try:
        people_amount = int(input("And how many people are gonna be with you during the stay? "))
    except ValueError:
        print("Please type a valid number!")
        continue
    if people_amount < 1 or people_amount > 6:
        print("Our capacity is between 1 and 6 people per apartment")
        continue
    break

while True:
    try:
        days_staying = int(input("And last but not least, for how long are you staying? "))
    except ValueError:
        print("Please type a valid number!")
        continue
    if days_staying < 1 or days_staying > 7:
        print("The stay must be between 1 and 7 days")
        continue
    break

# Processing - Calculate the daily rate and total cost
if type_APTO == 1:
    if people_amount == 1:
        daily = 20
    elif people_amount == 2:
        daily = 28
    elif people_amount == 3:
        daily = 35
    elif people_amount == 4:
        daily = 42
    elif people_amount == 5:
        daily = 48
    elif people_amount == 6:
        daily = 54
elif type_APTO == 2:
    if people_amount == 1:
        daily = 25
    elif people_amount == 2:
        daily = 34
    elif people_amount == 3:
        daily = 42
    elif people_amount == 4:
        daily = 50
    elif people_amount == 5:
        daily = 57
    elif people_amount == 6:
        daily = 63

total = people_amount * daily * days_staying

# Summary - Print the reservation details and total cost
print(f"\n===== Reservation Summary =====")
print(f"Guest name:       {name}")
print(f"Apartment type:   {type_APTO}")
print(f"Number of people: {people_amount}")
print(f"Days staying:     {days_staying}")
print(f"Daily rate:       R$ {daily:.2f}")
print(f"Total cost:       R$ {total:.2f}")
print(f"================================")
