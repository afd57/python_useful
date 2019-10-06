
# 1. Keyword Arguments

src: http://book.pythontips.com/en/latest/args_and_kwargs.html

 *args and **kwargs magic variables.

*args and **kwargs allow you to pass a variable number of arguments to a function.

What variable means here is that you do not know beforehand how many arguments can be passed to your function by the user so in this case you use these two keywords.


*arg  => array


 **kwargs => dictionary

**kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function. 

## When to use them?
The most common use case is when making function decorators (discussed in another chapter). 

Moreover it can be used in monkey patching as well. 

Monkey patching means modifying some code at runtime. 
Consider that you have a class with a function called get_info which calls an API and returns the response data. If we want to test it we can replace the API call with some test data

src: http://book.pythontips.com/en/latest/args_and_kwargs.html


# 2. Debugging
src: http://book.pythontips.com/en/latest/debugging.html

If you wanna debug your python script line by line you can set break point in your script.

Set Break Point:
import pdb

pdb.set_trace() #it is a break point :)

or you can run your script with "-m pdb" parameter, 
$python -m pdb debug_python.py

check debug_python.py script


# 3. Generators
src: 
https://medium.com/python-yaz-lar/python-generator-ve-i-teratorler-a53e59f7c5b1
http://book.pythontips.com/en/latest/generators.html
https://takopweb.com/python-yineleyiciler/

Iterable (yinelenebilir)
An iterable is any object in Python which has an __iter__ or a __getitem__ method defined which returns an iterator or can take indexes
iterable using the series s[0], s[1], s[2], ... until IndexError or StopIteration is raised.

Iterator (yineleyici)
An iterator is any object in Python which has a next (Python2) or __next__ method defined.

Iteration
When we use a loop to loop over something it is called iteration. It is the name given to the process itself. 

All of these parts are linked to each other. We will discuss them one by one and later talk about generators.

Generators
Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly. You use them by iterating over them, either with a ‘for’ loop or by passing them to any function or construct that iterates.

```python
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)
```

# 4 (set) Data Structure

set is a really useful data structure. sets behave mostly like lists with the distinction that **set can not contain duplicate values.** It is really useful in a lot of cases. 

Intersection
You can intersect two sets. For instance:
```python
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
# Output: set(['red'])
```

Difference

You can find the invalid values in the above example using the difference method.
```python
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
# Output: set(['brown'])
```

You can also create sets using the new notation:
```python
a_set = {'red', 'blue', 'green'}
print(type(a_set))
#Output: <type 'set'>
```

# 5 Function Annotations
https://docs.python.org/3/library/typing.html

For example, here is a simple function whose argument and return type are declared in the annotations:
```pyhton
def greeting(name: str) -> str:
    return 'Hello ' + name
```
Argument type and return type is important to understand function and to prevent mistakes. 
