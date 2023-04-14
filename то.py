import random

def generate_combinations(num_combinations):
    frequencies = [1218, 1177, 1145, 1237, 1184, 1235, 1185, 1205, 1212, 1156, 1233, 1211, 1173, 1173, 1178, 1164, 1223, 1141, 1146, 1182, 1251, 1202, 1114, 1201, 1211, 1173, 1157, 1215, 1219, 1207, 1134, 1175, 1188, 1247, 1198, 1182, 1224, 1180, 1169, 1137, 1145, 1184, 1179, 1264, 1202, 1208, 1178, 1226, 1238]

    combinations = []

    for i in range(num_combinations):
        comb = []
        while len(comb) < 6:
            rand_num = random.randint(1, 49)
            if rand_num not in comb:
                if frequencies[rand_num-1] > 0:
                    comb.append(rand_num)
                    frequencies[rand_num-1] -= 1
        combinations.append(comb)

    return combinations

# Пример за генериране на 5 комбинации
print(generate_combinations(5))