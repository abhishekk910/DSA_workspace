class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def element_at_end(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode

    def push_at(self, new_element, number):
        newNode = Node(new_element)
        if number < 1:
            print("\nposition should be >= 1.")
        elif (number == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, number-1):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("\nThe previous node is null.")

    def PrintList(self):
        temp = self.head
        if(temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

list = LinkedList()

list.element_at_end(10)
list.element_at_end(20)
list.element_at_end(30)

list.PrintList()