class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None 

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    def get(self, index: int) -> int:
        temp = self.head
        idx = 0
        while idx< index and temp!= None:
            temp = temp.next
            idx += 1
        if temp != None:
            return temp.value
        return -1

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        if self.head == None:
            self.head  = temp
        else:
            temp.next = self.head
            self.head = temp
            
    def addAtTail(self, val: int) -> None:
        temp = self.head
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            print("gg")
        else:
            while temp.next!= None:
                temp = temp.next
            temp.next = newNode
            
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            temp = self.head
            newNode = Node(val)
            idx = 1
            while idx < index:
                temp= temp.next
                idx += 1
            if temp != None:
                newNode.next = temp.next
                temp.next = newNode
        
    def deleteAtIndex(self, index: int) -> None:
        idx = 1
        temp = self.head
        while idx < index:
            temp = temp.next
            idx += 1
        if index == 0:
            self.head= self.head.next
        else :
            if temp != None and temp.next!= None:
                temp.next = temp.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)