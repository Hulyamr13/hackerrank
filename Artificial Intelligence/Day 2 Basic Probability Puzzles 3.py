from itertools import product
from fractions import Fraction

urns = [
    ['r']*4 + ['b']*3,  # Urn X
    ['r']*5 + ['b']*4,  # Urn Y
    ['r']*4 + ['b']*4   # Urn Z
]

# Get all possible combinations of one ball from each urn
combinations = product(*urns)

# Count the number of combinations that have 2 red balls and 1 black ball
count = sum(1 for c in combinations if c.count('r') == 2 and c.count('b') == 1)

# Calculate and print the probability
print(Fraction(count, len(urns[0])*len(urns[1])*len(urns[2])))