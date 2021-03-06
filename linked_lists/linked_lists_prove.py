class LinkedList:

    class Node:

        def __init__(self, data):

            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self,value):
        head = LinkedList.Node(value)

        if self.head ==  None:
            self.head = head
            self.tail = head

        else:
            head.next = self.head
            self.head.prev = head
            self.head = head

    ############# Prove 1 ###############
    def insert_tail(self,value):
        pass

    def remove_head(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.head != None:
            self.head.next.prev = None
            self.head = self.head.next

    ############# Prove 2 ###############
    def remove_tail(self):
        
        pass


    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


print("\nTEST 1")
print("-----------------\n")
ll = LinkedList()

ll.insert_head(5)
ll.insert_head(4)
ll.insert_tail(7)
ll.insert_head(3)
ll.insert_head(2)
ll.insert_tail(9)

print(ll) # Answer should be [2,3,4,5,7,9]

print("\nTEST 2")
print("-----------------\n")

ll.remove_head()
ll.remove_head()
ll.remove_tail()

print(ll) # Answer should be [4,5,7]

