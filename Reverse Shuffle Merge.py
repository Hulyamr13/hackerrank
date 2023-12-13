#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    s = list(reversed(s))
    remaining_dict,required_dict,added_dict = {},{},{}
    for c in s:
        if c not in remaining_dict:
            remaining_dict[c]=1
        else:
            remaining_dict[c]+=1
    for key,value in remaining_dict.items():
        required_dict[key] = value // 2
        added_dict[key] = 0
    char_list=[]
    index = 0
    min_index = 0
    min_char = '|'
    while index < len(s):
        char = s[index]
        if required_dict[char]>added_dict[char]:
            if char < min_char:
                min_char = char
                min_index = index
            if remaining_dict[char]-1<required_dict[char]-added_dict[char]:
                while index>min_index:
                    index-=1
                    char = s[index]
                    remaining_dict[char]+=1
                added_dict[char]+=1
                char_list.append(char)
                min_char = '|'
        remaining_dict[char]-=1
        index+=1
    return "".join(char_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()