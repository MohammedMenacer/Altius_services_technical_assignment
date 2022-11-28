from exercise1 import *


linkedList1Test1 = SinglyLinkedList()
linkedList2Test1 = SinglyLinkedList()

linkedList1Test2 = SinglyLinkedList()
linkedList2Test2 = SinglyLinkedList()


linkedList1Test1.append(3)
linkedList1Test1.append(2)
linkedList1Test1.append(2)
linkedList2Test1.append(3)
linkedList2Test1.append(2)
linkedList2Test1.append(2)

linkedList1Test2.append(2)
linkedList1Test2.append(1)
linkedList2Test2.append(1)
linkedList2Test2.append(2)


print(1 if linkedList1Test1.compare_lists(linkedList2Test1) else 0)
print(1 if linkedList1Test2.compare_lists(linkedList2Test2) else 0)
