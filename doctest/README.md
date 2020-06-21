# Python doctest 

Purpose: Write automated tests as part of the documentation for a module.

Mostly we use unittest while writing test even for very simple functions. `doctest` is very simple yet powerful, and it has practically no learning curve. `doctest` comes as build-in no extra dependencies required. Your test cases will provide example for the other developers. I thin, it can be usefull for TDD https://www.python-course.eu/python3_tests.php#Test-driven-Development-(TDD)

But `doctest` can't be used for complex test cases. 



The `doctest` module searches lines starting with “>>>” in `docstring` and runs them. A doctest will fail if the actual output does not match the expected output.

```python
def function():
    """
    >>> function(c) # write your testcase
    # write your expected result
  	"""
def hello_world():
  	"""
    >>> hello_world()
    helloWorld
    """
    print("helloWorld")
```



**Example:** fib.py

```python
def fib(n):
    """ 
    Calculates the n-th Fibonacci number iteratively  

    >>> fib(0) # test cases
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(15)
    610
    >>> 

    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def hello_world():
    """
    >>> hello_world()
    helloWorld
    """
    print("helloWorld")

```

Output

```tex
Trying:
    fib(15)
Expecting:
    610
ok
Trying:
    hello_world()
Expecting:
    helloWorld
ok
1 items had no tests:
    fib
2 items passed all tests:
   4 tests in fib.fib
   1 tests in fib.hello_world
5 tests in 3 items.
5 passed and 0 failed.
Test passed.

```



Fail Case

```python
File "/Users/mbp/Desktop/git/python_useful/doctest/fib.py", line 24, in fib.hello_world
Failed example:
    hello_world()
Expected:
    helloWorld3
Got:
    helloWorld
```



# Run in Jenkins



You should check execution result in automation system. It is a simple example for running this test in Jenkins.

```bash
#!/bin/bash

python3 -m doctest -v fib.py

if [ $? -ne 0 ]
then
   echo "Test Failed"
   exit 1
fi
```

