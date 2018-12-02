#!/usr/bin/python3
'''
The easiest way is for parsing XML to use xpath.
'''

import xml.etree.ElementTree as ET

root = ET.parse('data_camp.xml').getroot()

# I want to select 2010's comedy films ratings
print('----------------------2010\'s Comedy films rating----------------------')
comedy_films = root.findall('./genre/[@category="Comedy"]') # Selected all comedy movies
comedy_films_2010 = root.findall('./genre/[@category="Comedy"]/decade/[@years="2010s"]') # Selected only 2010's year comedy movies 
comedy_films_2010_rating = root.findall('./genre/[@category="Comedy"]/decade/[@years="2010s"]/movie/rating') # Selected 2010's year comedy movie's ratings

for rate in comedy_films_2010_rating:
    print(rate.text)


#I want to see category list
print('----------------------Category----------------------')
category_list = root.findall('./genre')
for category in category_list:
    print(category.attrib['category'])