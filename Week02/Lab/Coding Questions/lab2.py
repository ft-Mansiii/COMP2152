import random

# Define weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Roll the dice (1-6)
weaponRoll = random.randint(1, 6)
print(f"You rolled: {weaponRoll}")

# Calculate hero's combat strength assuming the initial value is 10
hero_combat_strength = 10 + weaponRoll
print(f"Hero's combat strength: {hero_combat_strength}")

# Determine hero's weapon
hero_weapon = weapons[weaponRoll - 1]
print(f"Hero's weapon: {hero_weapon}")

try:
    # Print weapon strength message
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Check if the weapon is not a Fist
    if hero_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")
except Exception as e:
    print(f"An error occurred: {e}")

