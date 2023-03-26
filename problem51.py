import math

ab = float(input())
bc = float(input())

ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0

angle_b_radian = math.acos(bc / (2*bm))

angle_b_degree = int(round((180 * angle_b_radian) / math.pi))

print(angle_b_degree,'\u00B0',sep='')