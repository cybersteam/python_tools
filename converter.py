import csv

with open('newmyfile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0])
    #with open('output.csv', 'w') as new_file:
        #we make a list called fieldnames here so we can pass it into the writer
        #below as the fieldnames argument. DictWriter then sets those as the headers.

            #fieldnames = []
            #fieldname = 'Field'
            #fieldnames.extend(line[1])
            #fieldnames.append(fieldname+'1')
            #print(fieldnames)
