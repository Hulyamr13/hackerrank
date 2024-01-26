import collections

numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def ranker(cards):
    suits = [i[-1] for i in cards]
    same_suit = len(set(suits)) == 1

    values = [numbers.index(i[0]) for i in cards]
    values.sort(reverse=True)

    if values == [12, 3, 2, 1, 0]:
        return (8, max(values)) if same_suit else (4, 3)

    differences = [values[i] - values[i + 1] for i in range(4)]
    differences.append(-1)

    groups = []
    start = 0
    for i in range(1, len(differences)):
        if differences[i] != differences[i - 1]:
            groups.append((differences[i - 1], i - start))
            start = i

    consecutive_values = (1, 4) in groups

    values_same = [i[0] for i in collections.Counter(values).most_common()]

    if same_suit and consecutive_values:
        return (8, max(values))
    elif (0, 3) in groups:
        return (7, *values_same)
    elif (0, 1) in groups and (0, 2) in groups:
        return (6, *values_same)
    elif same_suit:
        return (5, *values)
    elif consecutive_values:
        return (4, max(values))
    elif (0, 2) in groups:
        return (3, *values_same)
    elif groups.count((0, 1)) == 2:
        return (2, *values_same)
    elif (0, 1) in groups:
        return (1, *values_same)
    else:
        return (0, *values)


def sorter(player1, player2):
    size = min(len(player1), len(player2))
    for i in range(size):
        if player1[i] > player2[i]:
            return 'Player 1'
        elif player1[i] < player2[i]:
            return 'Player 2'


for _ in range(int(input())):
    cards = input().split()
    player1_cards = cards[:5]
    player2_cards = cards[5:]
    print(sorter(ranker(player1_cards), ranker(player2_cards)))
