#!/bin/python3

import sys


def times_sublist_in_list(sublist, l):
    pos_sublist = 0
    total = 0
    for i in range(0, len(l)):
        if sublist[pos_sublist] == l[i]:
            pos_sublist += 1
            if pos_sublist == len(sublist):
                total += 1
                pos_sublist = 0
        else:
            pos_sublist = 0
    return total


def search_trigram(words):
    max_total = 0
    max_trigram = []
    for i in range(0, len(words)):
        for j in range(0, len(words[i]) - 2):
            trigram = words[i][j:j + 3]
            total = 1
            total += times_sublist_in_list(trigram, words[i][j + 3:])
            for k in range(i + 1, len(words)):
                total += times_sublist_in_list(trigram, words[k])

            if total > max_total:
                max_total = total
                max_trigram = trigram
    return max_trigram


if __name__ == '__main__':
    s = sys.stdin.read()
    sentences = list(filter(lambda x: x != " ", s.split(".")))
    words = []
    for i in range(0, len(sentences)):
        words.append(
            [
                x.lower().strip()
                for x in sentences[i].split(" ")
                if x != ''
            ])

    print(" ".join(search_trigram(words)))