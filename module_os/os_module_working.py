# -*- coding: utf-8 -*-
"""os module example.

Author: Sir Aziz
Date: 2019-01-26

"""
import collections

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name='Aziz', field='math', born='boyabat', nobel=False)
)

source_path = ('''
%s/file1
%s/file2
%s/file3
%s/file4
%s/file5
%s/file6
%s/file7
%s/file8
%s/file9
%s/file10
%s/file11
''').split()

for path in source_path:
    print(path % 'source/dir/folder')
