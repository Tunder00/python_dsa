class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self ,value):
        # create a new node and initialise the LL
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)

# above given program can create a LL with one value but we cannot append prepend / insert
#  in the above example we have used a class called as node because while doing
# any operation on LL we will have to create a node so we have kept the node creation as a class