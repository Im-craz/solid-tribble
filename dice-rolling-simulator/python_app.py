import random


def roll_dice():
    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)

        print(f'dice rolled: {dice_one} and {dice_two}')

        roll = input("Roll again? (Yes/No): ")


roll_dice()
