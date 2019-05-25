import re

'''
The first metacharacter we will look at is . (dot). 
This matches any character, other than a new line.
'''
pattern = r"gr.y"
print('. metacharacter')
if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")
print('. metacharacter')

'''
The next two metacharacters are ^ and $.
These match the start and end of a string, respectively.
^(start)..........$(end)
(start) after ˆ
(end)   after $
'''
pattern = r"^gr.y$"
print(' ^ and $  metacharacter')
if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")


'''
Character Classes
Character classes provide a way to match only one of a specific set of characters.

A character class is created by putting the characters it matches inside square brackets.

**The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.**

'''

print('Character Classes')
pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")

'''
Character classes can also match ranges of characters. 
Some examples:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit. 
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
'''

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")

'''
The metacharacter ? means "zero or one repetitions".i

The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".

Fill in the blanks to match both 'color' and 'colour'.
pattern = r"colo(u)?r"

Curly braces can be used to represent the number of repetitions between two numbers.

'''
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

'''
Another important metacharacter is |.
'''

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")
