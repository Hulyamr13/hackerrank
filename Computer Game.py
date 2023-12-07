LIM = 32100
NUM = 123456

class Node:
    def __init__(self, x):
        self.x = x
        self.id = None
        self.next = None

class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

class List:
    def __init__(self):
        self.size = 0
        self.head = None

hash_table = [None] * NUM
p = []

def get_primes(limit):
    primes = [2, 3]
    for i in range(5, limit + 1, 2):
        for j in range(1, int(i ** 0.5) + 1):
            if i % primes[j] == 0:
                break
        else:
            primes.append(i)
    return primes

def get_id(x, iflag):
    b = x % NUM
    node = hash_table[b]
    while node:
        if node.x == x:
            return node.id
        node = node.next

    if iflag:
        new_node = Node(x)
        new_node.id = len(hash_table)
        new_node.next = hash_table[b]
        hash_table[b] = new_node
        return new_node.id
    return -1

def free_hash():
    for i in range(NUM):
        node = hash_table[i]
        while node:
            temp = node.next
            del node
            node = temp
        del hash_table[i]
    del hash_table

def insert(l, x):
    new_node = ListNode(x)
    new_node.next = l.head
    l.head = new_node
    l.size += 1

def free_list(l):
    node = l.head
    while node:
        temp = node.next
        del node
        node = temp

if __name__ == "__main__":
    p = get_primes(LIM)
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    hash_size = 0
    hash_table = [None] * NUM

