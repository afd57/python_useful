'''
Regular Expression Tutotial
'''
import re

'''
# match function
The re.match function can be used to 
determine whether it matches at the beginning of a string.
!!! beginning of the string !!!
'''

p_string = 'denemedenme'
if re.match(r'deneme', p_string):
    print('matched')
if re.match(r'denm', p_string):
    print('matched')
else:
    print('not matched')

'''
The function re.search finds a match of a 
pattern anywhere in the string.
'''
pattern = r"spam"
if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

'''
The function re.findall returns a list of all substrings 
that match a pattern.

The function re.finditer returns an iterator, rather than a list.
'''

print(re.finditer(pattern, "eggspamsausagespam"))

pattern = r'pam'
match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

'''
re.sub() function same as str.replace()
'''

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)
print(str.replace('David', 'Aziz'))

'''
********************************
Metacharacter
The first metacharacter we will look at is . (dot). 
This matches any character, other than a new line.
gr*y => gr.y
********************************
'''
pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(r"gr....y", "grrrrry"):
    print("Match 3")


'''
two metacharacters are ^ and $.
These match the start and end of a string, respectively.
^  =  start
$  =  end
pattern = r"^gr.y$"
Rules 
1) The string will start with 'gr'
2) The string will finish with 'y'
3) Have 4 letter

The pattern "^gr.y$" means that 
the string should start with gr, 
then follow with any character, 
except a newline, and end with y.

'''

pattern = r"^g..y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "grry"):
    print("Match 3")
