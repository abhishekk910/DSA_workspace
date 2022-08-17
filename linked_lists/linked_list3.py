class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_end(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                    temp = temp.next
            temp.next = newNode

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

    def delete_at_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None 

list = LinkedList()

list.add_at_end(10)
list.add_at_end(20)
list.add_at_end(30)
list.add_at_end(40)

list.PrintList()

list.delete_at_front()
list.PrintList()