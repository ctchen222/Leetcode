class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


# Init Linked List
head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(7)

head.next = A
A.next = B
C.next = C

# Traverse


def traverse_linked_list(head):
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next


print("---Traverse linked list---")
traverse_linked_list(head)

# Display


def display_linked_list(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    return "->".join(elements)


print("---Display linked list---")
print(display_linked_list(head))

# Search - O(n)


def search_linked_list(head, target):
    curr = head
    while curr:
        if curr.value == target:
            return True
        curr = curr.next
    return False


print("---Search linked list---")
print(search_linked_list(head, 1))
print(search_linked_list(head, 2))
