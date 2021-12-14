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
        
        # First, create a new node you will use as the tail
        tail = LinkedList.Node(value)
    
        # If there is no tail (which means the linked list is empty), set the head and tail to
        # the new node you created

        if self.tail == None:
            self.head = tail
            self.tail = tail

        # When there is already a tail:
            # Step 1 - Assign new node's prev to the current tail
            # Step 2 - Assign the current tail's next to the new node
            # Step 3 - Set the tail to the new node 
        else:
            tail.prev = self.tail
            self.tail.next = tail
            self.tail = tail

    def remove_head(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.head != None:
            self.head.next.prev = None
            self.head = self.head.next

    ############# Prove 2 ###############
    def remove_tail(self):

        # If head == tail (which means there is one item in the linked list)
        # set both the head and tail to none emptying the list.
        if self.head == self.tail:
            self.head == None
            self.tail == None
        
        # When there is more than one item in the linked list:
            # Step 1 - Assign the prev to the tail's next to None
            # Step 2 - Set the tail as the current tails previous
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev


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

