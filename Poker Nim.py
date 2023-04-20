def pokerNim(k, c):
    # Calculate XOR of chips in each pile
    score = 0
    for ctemp in c:
        score ^= ctemp

    # Check if score is 0 and return winner accordingly
    if score == 0:
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    t = int(input().strip()) # Number of test cases
    for i in range(t):
        n, k = [int(temp) for temp in input().strip().split(' ')] # Number of piles and maximum number of times a player can add chips
        c = [int(temp) for temp in input().strip().split(' ')] # Number of chips in each pile
        result = pokerNim(k, c) # Call the pokerNim function to get the winner
        print(result)