#Importing libraries
import os
import csv

#function that will retrieve a column from a csv file
#parameters: path to the file, index of column to be retrieved
#function considers the csv file contains headers
#function returns a list
def csv_column(csvpath, column):

    #opening the csv file
    with open(csvpath, newline='', encoding='UTF-8') as csvdata:
        column_name = []
        csvreader = csv.reader(csvdata, delimiter=',')
        next(csvreader) #skipping the header

        #for loop that will cycle through every row in the file
        for row in csvreader:
            column_name.append(row[column])
        return column_name

#setting ths csv path
csvpath = os.path.join('Resources', 'employee_data - copia.csv')

#retrieving the information for employee name
employee_name = csv_column(csvpath, 1)

#transformation from name into First and Last name
first_name = []
last_name = []

#splitting the string
for name in range(len(employee_name)):
    employee_name[name]= employee_name[name].split(' ', 2)

#storing first and last name
for name in employee_name:
    first_name.append(name[0])
    last_name.append(name[1])
