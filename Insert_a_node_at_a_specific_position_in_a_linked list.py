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

def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)

    # If the position is 0 or the list is empty, make the new node the head
    if position == 0 or llist is None:
        new_node.next = llist
        return new_node

    current = llist
    count = 0

    # Traverse the list to find the position
    while count < position - 1 and current.next is not None:
        current = current.next
        count += 1

    next_node = current.next
    current.next = new_node
    new_node.next = next_node

    return llist

def print_singly_linked_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())
    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head)
