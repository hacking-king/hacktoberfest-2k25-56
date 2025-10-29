import random

def roll_dice():
    print("🎲 Dice Roller 🎲")
    while True:
        input("Press Enter to roll...")
        print("You got:", random.randint(1, 6))
        again = input("Roll again? (y/n): ")
        if again.lower() != 'y':
            break

roll_dice()
