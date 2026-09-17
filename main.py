import random

while True:
    choice = input("Do you want to roll the dice? (y/n) ").lower()

    if choice == "y":
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        print(f"Dice One: {dice_one}, Dice Two: {dice_two}")
    elif choice == "n":
        print("Thank you for playing.")
        break
    else:
        print("Invalid choice!")
