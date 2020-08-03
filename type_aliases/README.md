# Python type hints

The Python runtime does not enforce function and variable type annotations. But this feature mostly reduce code readability. typing module comes from Python 3.5. This module provides runtime support for type hints that is define value type. I’m happy to see that it’s available in Python too.

The type hints proposal is [PEP 484](https://www.python.org/dev/peps/pep-0484/). The proposal describes the syntax for type annotations and the primary intent, which is enabling static code analysis.



The function below takes and returns a string and is annotated as follows:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

In the function `greeting`, the argument `name` is expected to be of type [`str`](https://docs.python.org/3/library/stdtypes.html#str) and the return type [`str`](https://docs.python.org/3/library/stdtypes.html#str). Subtypes are accepted as arguments.

You may lose flexibility on Python code, but your code will be more readable.



Practice:

```python
def my_sum(n1: int, n2: int) -> int:
    return n1 + n2

def my_div(n1:int, n2: int) -> float:
   return n1/n2
```





https://docs.python.org/3/library/typing.html

http://www.aylakhan.tech/?p=32