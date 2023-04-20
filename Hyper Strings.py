import os
import sys


#
# Complete the hyperStrings function below.
#
def hyperStrings(m, H):
    modul = 10 ** 9 + 7
    letters = "abcdefghij"
    H = [hyperstr for hyperstr in H if len(hyperstr) > 0]

    H_graded = {letter: [hyper_str for hyper_str in H if hyper_str[-1] == letter] for letter in letters}
    letter_graded = {letter: set() for letter in letters}
    for letter in letters:
        for hyper_end in H_graded[letter]:
            letter_graded[letter].add(hyper_end)
            for mid in letters:
                if mid == hyper_end[0]:
                    break
                to_add = [hyper_beg + hyper_end for hyper_beg in letter_graded[mid]]
                if to_add:
                    letter_graded[letter].update(to_add)

    dp = [{letter: 0 for letter in letters} for length in range(m + 1)]
    dp[0] = {letter: 1 for letter in letters}
    for length in range(1, m + 1):
        for letter, graded in letter_graded.items():
            for supstr in graded:
                if length < len(supstr):
                    continue
                dp[length][letter] = (dp[length][letter] + dp[length - len(supstr)][supstr[0]]) % modul
        for index in range(len(letters) - 1, 0, -1):
            dp[length][letters[index - 1]] = (dp[length][letters[index - 1]] + dp[length][letters[index]]) % modul
    return sum([dp[length]['a'] for length in range(m + 1)]) % modul


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    H = []
    while len(H) < n:
        H_item = input().split()
        H = H + H_item

    result = hyperStrings(m, H)
    fptr.write(str(result) + '\n')
    fptr.close()