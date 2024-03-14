import random

def roll():
    """simulates a fair dice roll"""
    lucky_number = random.randint(1,6)
    return lucky_number

# print(roll())


num_rolls = 10_000_000
total = 0

for i in range(num_rolls):
    total += roll()
    average = total / num_rolls

print(f" the average result of {num_rolls} rolls is {average}")
