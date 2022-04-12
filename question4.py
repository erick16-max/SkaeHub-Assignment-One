#Reading a csv file to a Dict

import csv
dict_data = []
def csv_to_dict():
    #path to csv
    csvFile = "csv_data.csv"

    #Open the file
    with open (csvFile) as csvFile:
        #Dict object of the data
        csvReader = csv.DictReader(csvFile)

        #iterate object to get dict rows
        for rows in csvReader:
            dict_data.append(rows)
    #returning a list with the dict_data
    return(dict_data)
dict_data = csv_to_dict()
print(dict_data)

        

