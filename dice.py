# Roll a dice

import random

def role_dice(sides):
    valid_dice = {4, 6, 8, 10, 12, 20, 100}
    
    if sides not in valid_dice:
        raise ValueError(f"Invalid dice! Choose from {valid_dice}.")

    return random.randint(1, sides)

#
print(role_dice(6))
print(role_dice(20))