import csv

#using the open function pass in the file and newline and create the variable csvfile
with open('thefile.csv', newline='') as csvfile:
    #create itemcounter and using csv.reader insert the file variable with delimiter and quotechar
    itemCounter = csv.reader(csvfile, delimiter=' ', quotechar='|' )

    next(itemCounter)
#THIS DIDNT QUITE WORK LETS DO IT AGAIN...
    for line in itemCounter:
        print(line[1])
