import math
from collections import defaultdict

def F(n, d):
    """
    Recursive function to calculate the value of F(n).

    Args:
    - n: int, the number for which F(n) is to be calculated.
    - d: defaultdict, a dictionary to store previously calculated values of F(n).

    Returns:
    - int, the value of F(n).
    """
    if n in d:
        return d[n]
    else:
        temp = 0
        for k in range(1, int(math.sqrt(n)) + 1):
            temp += F(n - k**2, d)
        d[n] = temp
        return d[n]


def towerBreakers(n):
    """
    Function to calculate the smallest value of 'ans' for which F(ans) >= n.

    Args:
    - n: int, the value of n for the current test case.

    Returns:
    - None, prints the value of 'ans' to the console.
    """
    ans = 0
    while d[ans] < n:
        ans += 1
    print(ans)


if __name__ == "__main__":
    d = defaultdict(int)
    d[0] = 1
    F(130, d)  # d[130] > 10**18

    for _ in range(int(input())):
        towerBreakers(int(input()))
