Source: 
https://www.sololearn.com/Play/Python
https://python-packaging.readthedocs.io/en/latest/
Section: Packaging

In Python, the term packaging refers to put modules you have written in a standard format, 
so that other programmers can install and use them with ease.

The first step in packaging is to organize existing files correctly. 
Place all of the files you want to put in a library in the same parent directory. 
This directory should also contain a file called __init__.py, which can be blank 
but must be present in the directory.
This directory goes into another directory containing the readme and license, as well as 
an important file called setup.py. 

In particular, packages should make it easy:
	To install with pip or easy_install.
	To specify as a dependency for another package.
	For other users to download and run tests.
	For other users to work on and have immediate familiary with the basic directory structure.
	To add and distribute documentation.

