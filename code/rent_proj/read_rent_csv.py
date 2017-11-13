# -*- coding:utf-8 -*-
import csv
import codecs

rentfile = 'rent.csv'
templist = []

with codecs.open(rentfile, "r") as f:
	templist = f.readline()

print(templist)
print(type(templist))
