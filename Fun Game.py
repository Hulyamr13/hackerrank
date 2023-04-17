def funGame(a, b):
    n = len(a)
    # Sort the indices in descending order based on a[i]+b[i]
    indices = sorted(range(n), key=lambda i: -(a[i]+b[i]))
    # Player 1 goes first, so they get the even indices and player 2 gets the odd ones
    p1_indices = indices[::2]
    p2_indices = indices[1::2]
    # Calculate the scores of both players
    p1_score = sum(a[i] for i in p1_indices)
    p2_score = sum(b[i] for i in p2_indices)
    if p1_score > p2_score:
        return "First"
    elif p1_score < p2_score:
        return "Second"
    else:
        return "Tie"


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        result = funGame(a, b)
        print(result)