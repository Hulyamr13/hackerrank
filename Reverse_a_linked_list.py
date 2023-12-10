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


def print_singly_linked_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next


def reverse(llist):
    prev = None
    current = llist

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist.head = reverse(llist.head)
        print_singly_linked_list(llist.head)
