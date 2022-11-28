class SinglyLinkedListNode:
    def __init__(self, d):
        self.data = d
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, nodeData):
        nodeAdded = SinglyLinkedListNode(nodeData)
        if self.head is None:
            self.head = nodeAdded
        else:
            last = self.head
            while (last.next):
                last = last.next
            last.next = nodeAdded

    def compare_lists(self, llist2):
        firstListNode = self.head
        secondListNode = llist2.head
        while (firstListNode != None and secondListNode != None):
            if (firstListNode.data != secondListNode.data):
                return False
            firstListNode = firstListNode.next
            secondListNode = secondListNode.next
        return (firstListNode == None and secondListNode == None)
