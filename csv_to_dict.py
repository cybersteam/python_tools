#This tutorial explains how to create a new csv based on certain criteria from two different fields
#Very useful
#https://www.youtube.com/watch?v=iy4N5Y3bRvA

import csv

file = open("daily_tick.csv","r")

my_dict_reader = csv.DictReader(file)


for row in my_dict_reader:
    print (row['DAILY'])
    print (row['04/11/20'])

#create dates from start of daily tick till present day as main keys
#add the stored data from the csv file into the appropriate dates
#if the row is a date, convert it to date format
#if the row is a date, convert it's fields to dictionaries according to space seperators









###???????????????????????????????
'''
for row in myreader:
	birds[row[1]] = {row[0],row[3]}



name = input("which bird?")
where = input("number or location?")

if name in people:
    print(people[name][where])
    '''
