#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#
class node2(dict):
    __slots__ = ['numDescendants']

    def __init__(self):
        self.numDescendants = 0

    def addChild(self, child):  # child is a character
        self[child] = node2()
        self.numDescendants += 1

    def getNumDescendants(self):
        return self.numDescendants

    def incNumDescendants(self):
        self.numDescendants += 1


class Contacts():
    def __init__(self):
        self.root = node2()

    def addName(self, name):
        def Helper(currNode, suffix):
            if len(suffix) == 0:
                currNode.addChild('')  # termination character
            else:
                if suffix[0] in currNode:
                    currNode.incNumDescendants()
                    Helper(currNode[suffix[0]], suffix[1:])
                else:
                    currNode.addChild(suffix[0])
                    Helper(currNode[suffix[0]], suffix[1:])

        currNode = self.root
        Helper(currNode, name)

    def findName(self, prefix):
        def findPrefix(currNode, prefix):
            if len(prefix) == 0:
                return currNode
            else:
                if prefix[0] in currNode:
                    return findPrefix(currNode[prefix[0]], prefix[1:])
                return -1

        nameLoc = findPrefix(self.root, prefix)
        if nameLoc == -1:
            return 0
        else:
            return nameLoc.getNumDescendants()


def contacts(queries):
    contactList = Contacts()
    result = []
    for query in queries:
        if query[0] == 'add':
            contactList.addName(query[1])
        elif query[0] == 'find':
            result.append(contactList.findName(query[1]))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
