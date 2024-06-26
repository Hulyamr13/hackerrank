#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    ptr1 = head1
    ptr2 = head2
    merged_head = None
    merged_tail = None

    if ptr1.data <= ptr2.data:
        merged_head = ptr1
        ptr1 = ptr1.next
    else:
        merged_head = ptr2
        ptr2 = ptr2.next

    merged_tail = merged_head

    while ptr1 and ptr2:
        if ptr1.data <= ptr2.data:
            merged_tail.next = ptr1
            ptr1 = ptr1.next
        else:
            merged_tail.next = ptr2
            ptr2 = ptr2.next
        merged_tail = merged_tail.next

    if ptr1:
        merged_tail.next = ptr1
    elif ptr2:
        merged_tail.next = ptr2

    return merged_head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
