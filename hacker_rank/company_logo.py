#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter
from collections import OrderedDict


if __name__ == '__main__':
    s = input()
    number_of_char = Counter(s)
    most_common_chars = number_of_char.most_common()
    tmp_list = []
    sorted_arry = []
    number_of_most_common_char = most_common_chars[1][1]
    total = 3
    for a,b in most_common_chars:
        if number_of_most_common_char == b:
            tmp_list.append(a)
        else:
            tmp_list.sort()
            for ch in tmp_list:
                sorted_arry.append((ch,number_of_most_common_char))
            tmp_list.clear()
            number_of_most_common_char = b
            tmp_list.append(a)
    if sorted_arry == []:
        tmp_list.sort()
        for ch in tmp_list:
                sorted_arry.append((ch,number_of_most_common_char))
    for i in range(total):
        print(f"{sorted_arry[i][0]} {sorted_arry[i][1]}")

# https://www.hackerrank.com/challenges/most-commons/problem
