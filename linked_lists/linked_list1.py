class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def add_element_at_front(self, newElement):
        newNode = Node(newElement)
        newNode.next = self.head 
        self.head = newNode   

    def PrintList(self):
        temp = self.head
        if (temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


list = LinkedList()

list.add_element_at_front(10)
list.add_element_at_front(20)
list.add_element_at_front(30)
list.PrintList() 
