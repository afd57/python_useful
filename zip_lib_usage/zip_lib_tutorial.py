#!/usr/bin/python3
# -*- coding: utf-8 -*-
from zipfile import ZipFile
"""
os module example.
Author: Sir Aziz
Date: 2019-09-15

Python zib libray usage and archive make

source 
https://www.geeksforgeeks.org/working-zip-files-python/
https://pymotw.com/3/zipfile/
https://www.datacamp.com/community/tutorials/zip-file

https://docs.python.org/3/library/shutil.html#archiving-operations
"""

# usage 1 shutil.make_archive
# make_archive(archive_name, 'gztar', root_dir)

import shutil
from pathlib import Path
import os

# create archihe
root_dir = Path("./basic").resolve()
base_dir = Path("./new_zip").resolve()
shutil.make_archive(base_dir, format='zip', root_dir=root_dir)


# extract archive
zip_path = Path("./new_zip.zip").resolve()
extact_path = Path("./deneme2").resolve()
shutil.unpack_archive(zip_path, extact_path, "zip")


# usage 2 zipfile module
file_name = "new_zip.zip"
extact_path_2 = Path("./zipfile").resolve()
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    print('Extracting spesified Demo -> 1 and HtmlDiff -> 2 dirs now...')
    for file in zip.namelist():
        if file.startswith('Demo/'):
            zip.extract(member=file, path=Path.joinpath(extact_path_2, "1"))
        elif file.startswith('HtmlDiff/'):
            zip.extract(member=file, path=Path.joinpath(extact_path_2, "2"))
    # zip.extractall(path=extact_path_2, members="Demo/")
    # zip.extract(member="Demo/Web.config")
    print('Done!')
