def calculate_damage(hps):
    hps = sorted(hps)
    s = 1
    total = sum(hps)
    for hp in hps:
        if (s + 1) * (total - hp) <= s * total:
            break
        s += 1
        total -= hp
    return s * total

def main():
    N = int(input())

    for n in range(N):
        input()  # Skipping unused input
        hps = list(map(int, input().split()))
        damage = calculate_damage(hps)
        print(damage)

if __name__ == "__main__":
    main()
