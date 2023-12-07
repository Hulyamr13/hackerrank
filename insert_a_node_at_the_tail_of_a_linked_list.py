class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)

    # If the list is empty, the new node becomes the head
    if head is None:
        head = new_node
        return head

    # Traverse to the end of the list
    current = head
    while current.next is not None:
        current = current.next

    # Append the new node at the end
    current.next = new_node

    return head


def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
