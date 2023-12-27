def update_seed(seed):
    return (seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)

def shift_seed(seed):
    return seed >> 17

def next_int(seed, n):
    return shift_seed(seed) % n

def find_seed(values):
    for lower_bits in range(2 ** 20):
        seed = lower_bits

        for value in values:
            seed = update_seed(seed)

            if (shift_seed(seed) & 7) != (value & 7):
                break
        else:
            for higher_bits in range(2 ** 28):
                seed = lower_bits | (higher_bits << 20)

                for value in values:
                    seed = update_seed(seed)

                    if next_int(seed, 1000) != value:
                        break
                else:
                    return seed

for _ in range(int(input())):
    values = list(map(int, input().split()))
    seed = find_seed(values)
    result = []

    for _ in range(10):
        seed = update_seed(seed)
        result.append(next_int(seed, 1000))

    print(' '.join(map(str, result)))
