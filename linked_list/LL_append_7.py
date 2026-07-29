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
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True #this is not mandatory
    
    # a method to print the whole linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
# before append
my_linked_list = LinkedList(1)
my_linked_list.print_list()
# after append
my_linked_list.append(2)
my_linked_list.print_list()
