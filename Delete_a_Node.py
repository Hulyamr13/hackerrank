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


def deleteNode(llist, position):
    # If the list is empty, return None
    if llist is None:
        return None

    # If position is 0, delete the head node
    if position == 0:
        return llist.next

    current = llist
    count = 0

    # Traverse the list to the node before the position to delete
    while count < position - 1 and current.next is not None:
        current = current.next
        count += 1

    # If the position is out of bounds, return the original list
    if current is None or current.next is None:
        return llist

    # Remove the node at the specified position
    current.next = current.next.next

    return llist


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist = deleteNode(llist.head, position)
    print_singly_linked_list(llist)
