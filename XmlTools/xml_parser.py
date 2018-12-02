#!/usr/bin/python37

import os
import sys
import xml.etree.ElementTree as ET


def xml_parser(xml_path='country_info.xml'):
    xml_path = 'country_info.xml'
    tree = ET.parse(xml_path)
    root = tree.getroot()
    print(root)


def rec_xml_parser(root,child_name,attr_name):
    for child in root.findall(child_name):
        print(child.tag,child.attrib['name'])
        

if __name__ == '__main__':
    try:
        path = 'country_info.xml'
        tree = ET.parse(path)
    except ex:
        print('Error')
    rec_xml_parser(tree.getroot(),'country','Panama')
