# DATABASE Project   
# David Bell
# EPortfolio CS 499

#!/usr/bin/python

import csv
import json



csvFilePath = 'test.csv'
jsonFilePath = 'end.json'

# read csv file and add the data to a dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        player = rows['player']
        data[player] = rows

# create new json file and write data on it
with open(jsonFilePath, 'w') as jsonFile:
    # make it more readable and pretty
    jsonFile.write(json.dumps(data, indent=4))

