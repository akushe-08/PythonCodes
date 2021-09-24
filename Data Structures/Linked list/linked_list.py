class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f'[ {self.display()} ]'

    def enqueue(self, new_data):
        temp = self.head
        new_node = Node(new_data)
        if temp is None:
            self.head = new_node
            return self
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return self

    def push(self, new_data):
        temp = self.head
        new_node = Node(new_data)
        new_node.next = temp
        self.head = new_node
        return self

    def dequeue(self):
        temp = self.head

        if temp is None:
            print("Linked list is already empty")
            return self
        temp2 = None
        while temp.next:
            temp2 = temp
            temp = temp.next
        temp2.next = None
        return self

    def pop(self):
        temp = self.head

        if temp is None:
            print("Linked list is already empty")
            return

        if temp.next is None:
            self.head = None
            return self

        self.head = temp.next
        return self

    def remove(self, key):
        temp = self.head

        if temp is None:
            print('Linked list is already empty')
            return self

        if temp.next is None:
            if temp.data == key:
                self.head = None
                return self
            else:
                print('Invalid Key')
                return self
        if temp.data == key:
            self.head = temp.next
            return self

        while temp.next:
            temp2 = temp
            temp = temp.next
            if temp.data == key:
                temp2.next = temp.next
                return self
        print('Invalid Key')
        return self

    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list is empty")
            return
        print('[', end=' ')
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print(']')
        return

# Stack Implementation


# leest = LinkedList()
# leest.push(1).push(2).push(3).push(4)
# leest.display()
# leest.pop()
# print('-'*10)
# leest.display()


# Queue Implementation

leest = LinkedList()
leest.enqueue(1).enqueue(2).enqueue(3).enqueue(
    4).enqueue(5).enqueue(6).enqueue(7)
leest.display()
leest.dequeue()
print('-'*10)
leest.display()
leest.remove(4)
leest.display()
