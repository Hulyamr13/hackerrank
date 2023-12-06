class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return 0

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return 0
        slow = slow.next
        fast = fast.next.next

    return 1

if __name__ == '__main__':

    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)
    node4 = SinglyLinkedListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    result = has_cycle(node1)
    if result:
        print("Lista sadrži ciklus.")
    else:
        print("Lista ne sadrži ciklus.")
