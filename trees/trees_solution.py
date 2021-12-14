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

        # When inserting into a tree, you want to first find if the
        # number is greater or lesser than the current node value. 

        # If the number is less than the current node data, then 
        # you see if there is node to the left of it. If there isn't,
        # You can insert the new node there. 

        if data < node.data:
            if node.left == None:
                node.left = BST.Node(data)

            # If there is a node to the left of the current node, then you 
            # have to recursivly call the function with the that left node as 
            # an argument.
            else:
                self._insert(data, node.left)

        # If the number is greater than the current node data, then 
        # you see if there is node to the right of it. If there isn't,
        # You can insert the new node there. 
        elif data > node.data:
            if node.right == None:
                node.right = BST.Node(data)

            # If there is a node to the right of the current node, then you 
            # have to recursivly call the function with the that right node as an 
            # argument.
            else:
                self._insert(data, node.right)
    ########### END ############

    def __contains__(self, data):
        
        return self._find_node(data, self.root)
    
    ###############################
    ######### Problem  2 ##########
    ###############################

    def _find_node(self, data, node):

        # First you need to see if the number you are looking for is equal to the current node.
        # If it is, it is in the tree! So return True
        if data == node.data:
            return True

        # If the number you are looking for is greater than the current node, you first want to see
        # if to the right of that node is empty. If it empty then you return False because the number you 
        # are looking for isnt there.
        elif data > node.data:
            if node.right == None:
                return False

            # If there is a node to the right of the current node, then call it recursively. 
            else:
                return self._find_node(data, node.right)

        # If the number you are looking for is less than the current node, you first want to see
        # if to the left of that node is empty. If it empty then you return False because the number you 
        # are looking for isnt there.
        elif data < node.data:
            if node.left == None:
                return False

            # If there is a node to the right of the current node, then call it recursively. 
            else:
                return self._find_node(data, node.left)   
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
