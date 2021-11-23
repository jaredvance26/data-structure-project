# Stacks

## Introduction
Stacks are a data structure with the behavior LIFO (Last in, First out). We can use stacks for a lot of operations with a reasonable performance. Stacks have various functions. To add to the stack, you use the append function. To delete from a stack, use the pop function. 


![Stack Diagram](images/stack.webp)
#### Plates example 

If you have a stack of plates, the first one you pick up goes becomes bottom. As you accumulate more plates then what happens when you need to set one down? You don't take it from the bottom, but rather the top. The same goes with stacks in data structures. 

## Examples of Stacks

To <strong>create</strong> a stack, simply initalize a list.

`stack = []`

To <strong>add</strong> to the stack, use the append function.

```
stack.append('a')
stack.append('b')
stack.append('c')
```

If you printed the stack it would result would be the following:

`['a','b','c']`

To <strong>delete</strong> from the stack, use the pop function.

```
stack.pop()
```




## Performance

#### Size Function

<strong>Size</strong> = .len()
```
stack = ['a', 'b', 'c']
size = len(stack)
```
In this example, the size would return 3. 



|Function|Performance|
|-------------|-------------|
|.append()|O(1)|
| .pop()|O(1)| 
|.len()|O(1)|


## Stacks Prove

## Conclusion


### Return  [Home](README.md)