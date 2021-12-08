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

![]()


## Performance

## Trees Prove

## Conclusion






#### [Return Home](README.md)