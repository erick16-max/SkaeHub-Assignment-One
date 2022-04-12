#Reading a csv file to a Dict

import csv

#path to csv
csvFile = "csv_data.csv"

#Open the file
with open (csvFile) as csvFile:
    #Dict object of the data
    csvReader = csv.DictReader(csvFile)

    #iterate object to get dict rows
    for rows in csvReader:
        print(rows)
        

