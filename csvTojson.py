#!/usr/bin/python

import csv, json

csvFilePath = "naxxData.csv"
jsonFilePath = "NaxxLootData.json"

# read the csv and add the datat to a dictionary...
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        player = csvRow["player"]
        data[player] = csvRow

# print(data)



# write data to json file
with open(jsonFilePath, "w") as jsonFile:
   jsonFile.write(json.dumps(data, indent=4))