class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

list_1 = LinkedList()
list_1.push(20)
list_1.push(4)
list_1.push(10)
list_1.push(25)
print('Given linked list')
list_1.printList()
print('Reverse of given linked list')
list_1.reverse()
list_1.printList()