class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertion (self, data):
        newNode = Node (data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
    def traversal (self):
        current = self.head
        while current:
            print (current.data, end = ' -> ')
            current = current.next
        print ('NULL')

    # Double Traversal
    def middleInsertion (self, element):
        if self.head is None:
            return
        
        newNode = Node (element)
        current = self.head
        length = 0

        while current is not None:
            length += 1
            current = current.next
        
        middle = length // 2 if length % 2 == 0 else (length+1) // 2

        current = self.head
        while middle > 1:
            current = current.next
            middle -= 1

        newNode.next = current.next
        current.next = newNode
        return
    
    def insertionHareTortoise (self, element):
        if self.head is None:
            return
        else:
            newNode = Node (element)
            slow, fast = self.head, self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        newNode.next = slow.next
        slow.next = newNode
        return

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertion (1)
    ll.insertion (2)
    ll.insertion (3)
    ll.insertion (4)
    ll.traversal ()
    # ll.middleInsertion (5)
    ll.insertionHareTortoise (5)
    ll.traversal ()