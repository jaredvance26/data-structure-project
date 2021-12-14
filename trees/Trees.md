# Trees

## Trees Introduction
Trees are an effective data structure that are similar to the concept of linked lists. The main difference is that trees are sorted while linked lists generally are not. There are a few types of tree data structures, but we are going to focus on a <strong>Binary Search Tree (BST)</strong> for this lesson.

## Recursion

To first understand trees, one must be familiar with recursion. Recursion is the process of calling the function from within itself.

For example: 
```
def say_hello():
    print("hello")
    say_hello()
```

In this example, "hello" will be outputed until there is a recursion error displayed. But without the error, the "hello" statement would be outputed forever. Because of that, we need a <strong>base case</strong>. 


![Gif](images/giphy.gif)

A base case is a situation which allows the function call to end. 

For example:
```
def say_hello(count):
    if count <= 0:
        quit()
    else:
        print("hello")
        say_hello(count - 1)
```

In our example, the base case is the `if count <= 0`. We recursivly call the say_hello function until the base case requirements are met.

Normally, recursive statements are not very effective. But they could be used to for important tasks, such as searching trees.


## Example of Trees

How trees work is that you have the first number called the <strong>Root</strong>. When you add another number, if it is bigger than the root, it goes to the <strong>right</strong> while if it is smaller, it goes to the <strong>left</strong>. The added number is referred to as the <strong>child</strong> of the root. If you add another number, then it goes down the tree until it finds an open spot. The diagam below illustrates this principle.

![trees](/trees/images/tree.PNG)

### Inserting into the Tree
To insert into a tree, one must find recursively go down the tree in order to find a spot available. For example, if we wanted to insert a 17 in the diagram above we know that 17 is bigger than the root, 15, so we go <strong>right</strong>. Right of 15, there is no open spot but rather a 20. So now we need to go from 20 to see if there is an open spot. So 17 is less than 20, so we go <strong>left</strong>. Left of 20 is open, so that is where we will place it. The diagram below shows where 17 is placed.

![trees_ex](/trees/images/tree_ex.PNG)

Similarly, deleting and trying to see if something is in the tree requires using recurrsion.


## Performance

|Function|Performance|
|----------------|----------------|
|inserting into the tree|O(log(n))|
|removing from the tree|O(log)| 
|finding from tree |O(1)|
|size| O(1)|

It is important to note that this is the performance of a <strong> balanced </strong> tree. If the tree is not balanced, then then the performance is altered. If you insert a sorted list, then the tree will not be balanced. For example if you inserted 1,2,3,4,5 it would look like the diagram below.

![bad_tree](/trees/images/bad_tree.PNG)
## Trees Prove

For the [prove](trees_prove.py) assignment you will complete the _insert() and _find_node() functions.

For the _insert() function, you have to use recurrsion to find an empty spot to put a new node.

For the _find_node() function you have to use recurrsion to find a node. If the node is found, True is returned. Else, the function should return False.

After trying for <strong>at least 30 minutes</strong>, use the [solution](trees_solution.py) for reference.

## Conclusion

Trees are a very effective and useful data structure. They are very efficient, but can be difficult to understand. One must really understand recurrsion when dealing with trees. It is also noted that balanced BST are what are very effective. If it isn't balanced, its performance drops. 





#### [Return Home](/README.md)