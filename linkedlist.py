class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None :
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ->")
            temp = temp.next
        print("None")


    def insertBegin(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, val):
        temp = self.head
        prev = None
        
        if temp != None and temp.data == val:
            self.head = temp.next
            temp = None
            print(f"{val} has been deleted from the linkedlist")
            return 

        while temp != None and temp.data != val:
            prev = temp
            temp = temp.next

        if temp == None:
            print(f"{val} not found in the list")
            return 

        prev.next = temp.next
        temp = None
        print(f"{val} has been deleted from the list")
        
if __name__ == "__main__":
    link = linkedList()
        
    link.append(20)
    link.append(30)
    link.append(50)
    link.append(40)
    link.append(60)

    print("Original LinkedList: ")
    link.display()

    link.insertBegin(10)
    print(" List after prepending: ")
    link.display()

    link.delete_by_value(10)
    print("List after deleteion: ")
    link.display() 

    link.delete_by_value(60)
    print("List after deleteion: ")
    link.display() 

    link.delete_by_value(100)
    print("List after deleteion: ")
    link.display() 


