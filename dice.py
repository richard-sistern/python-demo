# Roll a DnD dice

import random

def roll_dice(sides):
    valid_dice = {4, 6, 8, 10, 12, 20, 100}
    
    if sides not in valid_dice:
        raise ValueError(f"Invalid dice! Choose from {valid_dice}.")

    return random.randint(1, sides)

def roll_with_advantage(sides):
    """Rolls a D&D die twice and returns the higher result (Advantage)."""
    roll1 = roll_dice(sides)
    roll2 = roll_dice(sides)
    print(f"Advantage rolls: {roll1}, {roll2}")
    
    return max(roll1, roll2)

def roll_with_disadvantage(sides):
    """Rolls a D&D die twice and returns the lower result (Disadvantage)."""
    roll1 = roll_dice(sides)
    roll2 = roll_dice(sides)
    print(f"Disadvantage rolls: {roll1}, {roll2}")
    
    return min(roll1, roll2)

# Example usage
print(f"Regular roll result: {roll_dice(20)}")  # Rolls a d20
print(f"Advantage roll result: {roll_with_advantage(20)}")  # Rolls with advantage
print(f"Disadvantage roll result: {roll_with_disadvantage(20)}")  # Rolls with disadvantage