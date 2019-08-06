# -*- coding: utf-8 -*-

from csv import*

csvInstance = csv()

content = csvInstance.generateRandomCSV()

print (content)

f = open("csv.csv","w")
f.write(content)
f.close()