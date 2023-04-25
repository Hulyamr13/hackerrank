def g(diff):
    ans = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
    return diff // 5 + ans[diff % 5]

def f(chocolates, goal):
    return sum(g(chocolate-goal) for chocolate in chocolates)

def get_ans(chocolates):
    min_chocolate = min(chocolates)
    return min(f(chocolates, min_chocolate - dc) for dc in range(4))


if __name__ == '__main__':
    T = int(input(""))
    for i in range(T):
        N = int(input(""))
        inp = input("").split()
        chocolates = [int(chocolate) for chocolate in inp]
        print(get_ans(chocolates))
