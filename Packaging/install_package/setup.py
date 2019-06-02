#!/usr/bin/env python

from distutils.core import setup


## install single script
setup(name='aziz_compress_and_hashes',
      version='1.0',
      description='Aziz Packge Installing',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      #py_module=['sha1'] #Yukleyecegimiz scriptleri .py uzantisi olmadan buraya ekleyecegiz.
      # py_module https://docs.python.org/3/distutils/setupscript.html#listing-individual-modules
      packages=['compression', 'hashes'],
      # eger paket yukleyeceksek packages parametresini paketleri liste seklinde ekleyecez
)

# import hashes.md5 bu sekilde import ediliyor