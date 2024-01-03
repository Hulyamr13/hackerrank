# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

mean = 20
std_dev = 2

def calc_prob(lower_bound, upper_bound=None):
    if upper_bound is None:
        prob = 0.5 * (1 + math.erf((lower_bound - mean) / (std_dev * math.sqrt(2))))
    else:
        prob = 0.5 * (math.erf((upper_bound - mean) / (std_dev * math.sqrt(2))) -
                             math.erf((lower_bound - mean) / (std_dev * math.sqrt(2))))
    return prob

print(round(calc_prob(19.5), 3))
print(round(calc_prob(20, 22), 3))
