import csv

## THIS ACTUALLY WORKS!

with open('myfile.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    with open('output.csv', 'w') as new_file:
        #we make a list called fieldnames here so we can pass it into the writer
        #below as the fieldnames argument. DictWriter then sets those as the headers.

        fieldnames = ['Date','Expense 1','Expense 2','Expense 3']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        #for each line in the csv_reader obj
        #make the line corresponding to each fieldname do what you want it to be.
        for line in csv_reader:
            #line['Date'] = line['Date']+'hey it work'
            line['Expense 1'] = '-'+line['Expense 1']
            line['Expense 2'] = '-'+line['Expense 2']
            line['Expense 3'] = '-'+line['Expense 3']
            csv_writer.writerow(line)

'''
    with open('output.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')
        for line in csv_reader:
            if [0] > 0:
                print(line[1],[2],[3])
            #csv_writer.writerow(line)

### This piece from Corey Schafer shows the basic reader and writer nicely - the DictReader
# and DictWriter are probably better for most stuff though.
#opens the file as read 'r' and puts it into csvfile
with open('myfile.csv', 'r') as csv_file:
    #creates csv_reader which runs the reader method with the file and it's delimeters
    csv_reader = csv.reader(csv_file, delimiter=',')
    #calling next steps over a value of an iterable - somehow jumps the first line
    #next(csv_reader)
    with open('output.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')
    #print(csv_reader)
        #for each line of the original data in csv_reader -
        #then write a row in new file with each line of the original
        for line in csv_reader:
            csv_writer.writerow(line)





line_count = 0
for row in csv_reader:
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        line_count += 1
print(f'Processed {line_count} lines.')




import pandas as pd
df = pd.read_csv("myfile.csv", index_col=0)
number = df.loc[df[2]]
if number == int:

print(number==int] = -abs(number))



#number = float


#df.head(4) #prints 4 heading rows
#If you want to change all the values, where 'Ip' is equal to 127.0.0.2, run:
#df.loc[df["date1"]==number, "date1"] = -abs(number)
#df.to_csv("output.csv", index=False)







   Ip  Sites
0   127.0.0.1   10
1   127.0.0.2   23
2   127.0.0.3   50




#Now if you want to change the value in the 'Sites' column in the 1st row, run:
#df.set_value(1, "Sites", 30)
df.set_value()
#If you want to change all the values, where 'Ip' is equal to 127.0.0.2, run:
df.loc[df["Ip"]=="127.0.0.2", "Sites"] = 30
#Finally, to save the values:
df.to_csv("output.csv", index=False)




import csv

r = csv.reader(open('myfile.csv')) # Here your csv file
lines = list(r)

if lines[4:233][2:] == float:
    lines = -abs(lines)
    writer = csv.writer(open('output.csv', 'w'))
    writer.writerows(lines)






###########################

thefile = open('myfile.csv')
thereader = csv.reader(thefile, delimiter=',', newline='')
theline = 0

for row in csv_reader:
    if


with open('myfile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', newline='')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

March:
Opening: 5,390.16
Closing: 153,644.45

April:
Opening: 153,644.45
Closing: 194,107.57

May:
Opening: 194,107.57
Closing: 213,518.32

June:
Opening: 213,518.32
Closing: 225,553.52
'''
