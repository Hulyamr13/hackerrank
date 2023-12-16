#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    root = {}

    def add_to(root, s):
        current_node = root.setdefault(s[0], [0, {}])
        if len(s) == 1:
            current_node[0] += 1
        else:
            add_to(current_node[1], s[1:])

    def is_prefix(root, s):
        if len(s) == 1:
            if len(root[s[0]][1]) > 0 or root[s[0]][0] > 1:
                return True
            else:
                return False
        else:
            if root[s[0]][0] > 0:
                return True
            else:
                return is_prefix(root[s[0]][1], s[1:])

    count = 0

    for word in words:
        add_to(root, word)
        if is_prefix(root, word):
            return ["BAD SET", word]
        count += 1

    if count == len(words):
        return ["GOOD SET"]

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    result = noPrefix(words)

    for item in result:
        print(item)
