
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


## 2. Debugging

If you wanna debug your python script line by line you can set break point in your script.

Set Break Point:
import pdb

pdb.set_trace() #it is a break point :)

or you can run your script with "-m pdb" parameter, 
$python -m pdb debug_python.py

check debug_python.py script

