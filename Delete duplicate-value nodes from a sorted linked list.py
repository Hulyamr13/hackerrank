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


def removeDuplicates(llist):
    current = llist
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return llist


def print_singly_linked_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist = removeDuplicates(llist.head)
        print_singly_linked_list(llist)
