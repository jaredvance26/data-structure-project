# Big-O-Notation

## Introduction
Big-O-Notation is a way to measure the performance of a program. A program can work, but it does not mean that it runs effectively. This especially gets important as you work with bigger data.

## Performance Levels

### O(n)
<strong>O(n)</strong> performance is ok when it comes to small datasets. The larger the data, the less efficent it becomes.

![O(n) graph](/big_o_notation/images/O(n).png)

As you can see in the graph, where x is amount of work, and y is is the amount of data. The bigger the amount of data, the amount of work grows a lot. 

This is an O(n) occurence:
```
for x in list:
    print(x)
```
If the list is very large, it will take a lot of work. If it small, then there it will get the job done relatively well. 

### O(n<sup>2</sup>)

<strong>O(n<sup>2</sup>)</strong> is not effective and should be avoided when writing code. As the amount of data is rises, the amound of work grows exponentially. 

![O(n<sup>2</sup>) graph](/big_o_notation/images/O(n^2).png)

As you can see in the graph, where x is amount of work, and y is is the amount of data. The bigger the amount of data, the amount of work grows exponentially.

This is an O(n<sup>2</sup>) occurence:
```
for x in list:
    for y in list_two:
        print(x,y)
```

O(n<sup>2</sup>) is not an effective way to code and can lead to slower loading rates.

### O(log(n))
<strong>O(log(n))</strong> is a very efficent way to to code. If you have a big list of sorted numbers, and you are looking for a random number, it essentially keeps on halfing the data set until the random number is found. So instead of looping through the whole data set, it goes straight to the middle. If the number is bigger than the middle, it only then looks for in the bigger half of the set.

![O(log(n)) graph](/big_o_notation/images/O(log(n)).png)

This is a very effective way to code. A larger data set doesn't create a much bigger work load.


### O(1)

Lastly is <strong>O(1)</strong> performance. This is the best and most efficent way to code. If you are looking for a certain number in a dataset, it is finding the number first.

![O(1) graph](/big_o_notation/images/O(1).png)

This is the best case performance but can be the most difficult to carry out. 

##### [Return Home](/README.md)