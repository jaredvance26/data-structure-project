# Trees

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

In our example, the base case is the ` if count <= 0`. We recursivly call the say_hello function until the base case requirements are met. 

## Example of Trees


## Performance

## Trees Prove

## Conclusion






##### [Return Home](README.md)