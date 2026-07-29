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
    # a method to print the whole linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
my_linked_list.print_list()