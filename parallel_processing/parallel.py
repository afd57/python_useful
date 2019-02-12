# -*- coding: utf-8 -*-
"""Parallel Processing with "concurrent.futures.

Author: Aziz
Date: 2019-01-26

How to do multithreading and parallel programming in Python
using functional programming principles and the "concurrent.futures" module.

Important:
Python "Global Interpreter Lock", also known as the "GIL"

"""
import collections
import multiprocessing
import concurrent.futures
import os
import time
from pprint import pprint

Employee = collections.namedtuple('Employee', [
    'name',
    'field',
    'born',
])

employees = (
    Employee(name='Aziz', field='ast.engineer', born='Ankara'),
    Employee(name='Mehmet', field='engineer', born='Eskisehir'),
    Employee(name='Ahmet', field='sr.engineer', born='Istanbul')
)


def backup_employees_data(employees):
    print(f'Process {os.getpid()} backup {employees.name}')
    time.sleep(1)  # connection and write to db
    print(f'Result {os.getpid()} finish. {employees.name} saved to db')
    return 1


start = time.time()

# pool = multiprocessing.Pool()
# result = pool.map(backup_employees_data, employees)
# result: backup is completed: 1.028s different PID
# Process 3112 backup Aziz
# Process 3113 backup Mehmet
# Process 3114 backup Ahmet

# process based parallelism
""" in this case have global interpreter lock problem
because every single process has own interpreter therefore
they can all run in parallel you can actually spread them out across
multiple CPU cores and this solves the global interpreter lock problem

"""
# with concurrent.futures.ProcessPoolExecutor() as executor:
#    result = executor.map(backup_employees_data, employees)
# result: backup is completed: 1.039s different PID same as previous code,

# thread based parallelism

with concurrent.futures.ThreadPoolExecutor() as executor:
    result = executor.map(backup_employees_data, employees)
# result: backup is completed: 1.008s same PID.
end = time.time()

print(f'\n backup is completed: {end - start:.3f}s \n')
