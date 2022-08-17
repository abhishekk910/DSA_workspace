class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_end(self, new_element):
        newNode = Node(new_element)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode

    def countNodes(self):
        temp = self.head
        i = 0
        while (temp != None):
            i += 1
            temp = temp.next
        return i   
    
    def delete_at(self, number):
        if (number == 1 and self.head != None):
            node_to_delete = self.head 
            self.head = self.head.next
            node_to_delete = None 
        else:
            temp = self.head
            for i in range(1, number-1):
                if (temp != None):
                    temp = temp.next
            if (temp != None and temp.next != None):
                node_to_delete = temp.next
                temp.next = temp.next.next
                node_to_delete = None 
            else:
                print("Node is Null")

    def deleteAllNodes(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        print("All nodes are deleted successfully.") 
        
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

list.add_at_end(10)
list.add_at_end(20)
list.add_at_end(30)

list.PrintList()
print(f"Number of Nodes : ", list.countNodes())

# list.delete_at(2)
# list.PrintList()

# list.delete_at(1)
# list.PrintList()
list.deleteAllNodes()
list.PrintList()

