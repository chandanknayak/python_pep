class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class CircularLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             new_node.next = self.head
#             return

#         temp = self.head
#         while temp.next != self.head:
#             temp = temp.next
#         temp.next = new_node
#         new_node.next = self.head

#     def count_nodes(self):
#         if self.head is None:
#             return 0

#         count = 1
#         temp = self.head.next
#         while temp != self.head:
#             count += 1
#             temp = temp.next
#         return count

#     def display(self):
#         if self.head is None:
#             print("Circular Linked List is empty")
#             return

#         temp = self.head
#         while True:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#             if temp == self.head:
#                 break
#         print("(back to head)")


# # Example usage
# cll = CircularLinkedList()
# cll.append(10)
# cll.append(20)
# cll.append(30)

# cll.display()
# print("Total nodes:", cll.count_nodes())

def count_n(head):
    if head is None:
        return 0

    count = 0
    current = head
    while True:
        count += 1
        current = current.next
        if current == head:
            break
    return count