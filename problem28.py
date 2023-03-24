def minion_game(string):
    s = len(string)
    vowel_score = 0
    consonant_score = 0

    for i in range(s):
        if string[i] in 'AEIOU':
            vowel_score += (s - i)
        else:
            consonant_score += (s - i)

    if vowel_score < consonant_score:
        print('Stuart ' + str(consonant_score))
    elif vowel_score > consonant_score:
        print('Kevin ' + str(vowel_score))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)