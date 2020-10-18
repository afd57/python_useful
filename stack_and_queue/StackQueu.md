# Stack & Queue in Python

![File:QUEUE VS STACK.png](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/QUEUE_VS_STACK.png/800px-QUEUE_VS_STACK.png)

A stack is a linear data structure that stores items in a Last-In/First-Out (**LIFO**) or First-In/Last-Out (**FILO**) manner. In stack, a new element is added at one end and an element is removed from that end only.



Like stack, queue is a linear data structure that stores items in First In First Out (**FIFO**) manner. With a queue the least recently added item is removed first. 



**How to implement in Python?** It is  possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque) which was designed to have fast appends and pops from both ends. For example:

```python
from collections import deque
#------------------Queue----------------------------
queue = deque(["Aziz", "David", "Michael"])
queue.append("Ozenc")
queue.append("Ahmet")           # Append Items
queue.popleft()                 # first in first out.
queue                           # Remaining queue in order of arrival

#------------------Stack----------------------------
stack = deque(["Aziz", "David", "Michael"])
stack.append("Ozenc")
stack.pop()                     # Last in first out

#----------------------------------------------------

```



# When do you need stack?

We commanly use queue in our application, there are a lot of visible use case in the world. RabbitMQ is greate example. We use stack more than queue in our life but it is not visible **Ctrl + Z**  :). It has very important role in our life :) Let we check usage of stacks.

- Undo operation. 
- Web Browser back page operation

I have two daily example, if you have new, you can add it to list. 





