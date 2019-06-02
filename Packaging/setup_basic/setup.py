#!/usr/bin/env python

from distutils.core import setup


## install single script
setup(name='aziz_sha1',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      py_module=['sha1'] #Yukleyecegimiz scriptleri .py uzantisi olmadan buraya ekleyecegiz.
      # py_module https://docs.python.org/3/distutils/setupscript.html#listing-individual-modules
      #packages=['distutils', 'distutils.command'],
      # eger paket yukleyeceksek packages parametresini paketleri liste seklinde ekleyecez
)

# sha1.py script i Lib\site-packages'e install edilecek
# import sha1 seklinde import ediliyor