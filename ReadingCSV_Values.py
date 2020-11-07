
import csv

filename = "Details.csv"
mode = "r"
with open(filename,mode) as mycsvfile:
    dataFromFile = csv.reader(mycsvfile)
    for value in dataFromFile:
        for word in value:
            print(word)
        #print(value)