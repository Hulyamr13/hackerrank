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

def getNode(llist, positionFromTail):
    length = 0
    current = llist
    while current:
        length += 1
        current = current.next

    current = llist
    for _ in range(length - positionFromTail - 1):
        current = current.next

    return current.data

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)
        print(result)
