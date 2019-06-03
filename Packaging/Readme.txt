Source: 
https://www.sololearn.com/Play/Python
https://python-packaging.readthedocs.io/en/latest/
https://yazilimhanem.com/python-moduller/
https://metehan.us/python-kurulum-betigi-hazirlamak.html
https://docs.python.org/3/distutils/setupscript.html
https://docs.python.org/3/distutils/apiref.html#distutils.core.setup
http://www.gulsahkose.com/2015/01/python-paketi-hazrlamak.html
http://pythontr.blogspot.com/2008/11/setuppy-dosyas-hazrlamak.html
https://docs.python.org/3/install/
https://docs.python.org/3/distutils/setupscript.html
https://docs.python.org/3/distutils/introduction.html#distutils-simple-example
https://www.youtube.com/watch?v=4fzAMdLKC5k
https://www.youtube.com/watch?v=GeYis4ZuluY
https://www.youtube.com/watch?v=UKXx4e9PotI



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

