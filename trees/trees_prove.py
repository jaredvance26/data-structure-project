class BST:
    
    class Node:

        def __init__(self,data):
            self.data = data
            self.right = None
            self.left = None
        
    def __init__(self):
        self.root = None
    

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###############################
    ######### Problem  1 ##########
    ###############################

    def _insert(self,data,node):

        # This function with insert a value into a tree
        pass

    ########### END ############

    def __contains__(self, data):
        
        return self._find_node(data, self.root)
    
    ###############################
    ######### Problem  2 ##########
    ###############################

    def _find_node(self, data, node):
        
        # This function with see if a value is in the tree. Returns True if it is, and False if it isn't.
        pass

    ########### END ############


    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
    
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

tree = BST()
print("----------- Test 1 ------------\n")
tree.insert(15)
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(14)
tree.insert(17)
tree.insert(25)

for x in tree:
    print(x) # Answer: 5,10,14,15,17,25

print("----------- Test 2 ------------\n")

print(tree.__contains__(15)) 
print(tree.__contains__(35))
print(tree.__contains__(10))
print(tree.__contains__(19))

# Answer True, False, True, False
