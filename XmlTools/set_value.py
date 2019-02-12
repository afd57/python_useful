#!/usr/bin/python3
'''
Set xml element attribute
'''
import xml.etree.ElementTree as ET

tree = ET.parse('travel.xml')
root = tree.getroot()
root.findall(
    './country/[@name="Turkey"]/visitor/[@name="AzizBey"]')[0].attrib['name'] = 'Aziz'

tree.write('travel.xml')
