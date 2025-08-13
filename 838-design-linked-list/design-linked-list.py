class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
       
class MyLinkedList:

    def __init__(self):
        self.head = None

    def show(self):
        curr = self.head
        while curr:
            print(curr.val, end = ' -> ')
            curr = curr.next
        print('end')
    
       
    
    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr= curr.next
            count += 1
        return -1   
    
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        # self.show()

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr=self.head
        
        while curr and curr.next:
            curr = curr.next
        if curr:    
            curr.next = new_node
        else:
            self.head = new_node      
        # self.show()  

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        curr = self.head
        count = 0
        if index == 0:
            self.addAtHead(val)
            return 
        while curr and count < index - 1:
            count += 1
            curr = curr.next
        if curr:
            new_node.next = curr.next
            curr.next = new_node
        # self.show()    
      
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        count = 0
        if index == 0 and curr:
            self.head = curr.next
            return
        while curr  and count < index -1  :
            curr = curr.next
            count += 1
        if curr and curr.next:
            curr.next = curr.next.next
        # self.show()    
      


        