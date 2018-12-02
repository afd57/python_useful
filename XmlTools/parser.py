#source: https://gist.github.com/adrianp/1791262

import sys
# http://docs.python.org/library/xml.etree.elementtree.html
from xml.etree import ElementTree

def operation(node):
    """Just a sample function that prints the tag of a node."""
    return print(node.tag)
def recur_node(node, f):
    """Applies function f on given node and goes down recursively to its 
       children.
        
       Keyword arguments:
       node - the root node
       f - function to be applied on node and its children

    """
    if node != None:
        f(node)
        for item in node.getchildren():
            recur_node(item, f)
    else:
        return 0

def main(fileName):
    try:
        root = ElementTree.parse(fileName).getroot()
    except:
        # there should be some proper exception handling here
        return -1
    return recur_node(root,operation)

if __name__ == "__main__":
  sys.exit(main('country_info.xml'))
