#!/usr/bin/python37
'''
Compare three or more string with eachother.
if a==b and a==c and b==c: ===> if compare_strings[a,b,c]:
'''
def compare_strings(string_list):
    if type(string_list) != list:
        print(F"Please give a list as argument! Argument Type = {string_list}")
    else:
        list_item = string_list.pop()
        print(string_list)
        if list_item not in string_list:
            return False
        else:
            return True
