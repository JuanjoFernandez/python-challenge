#Importing libraries
import os
import csv
from us_state_abbrev import us_state_abbrev

#setting ths csv path
csvpath = os.path.join('Resources', 'employee_data - copia.csv')

#variable initialization
employee_id = []
first_name = []
last_name = []
dob_new = []
ssn_new = []
state_new = []

#opening the csv file
with open(csvpath, newline='', encoding='UTF-8') as csvdata:
    column_name = []
    csvreader = csv.reader(csvdata, delimiter=',')
    next(csvreader) #skipping the header

    #for loop that cycles through every row and creates the new lists of data
    for row in csvreader:
        employee_id.append(row[0]) #copies the employer id

        #splitting the name into first and last name
        employee_name = row[1]
        employee_name = employee_name.split(' ', 2)
        first_name.append(employee_name[0])
        last_name.append(employee_name[1])

        #reformatting date of birth into MM/DD/YYYY
        dob_old = row[2]
        dob_old = dob_old.split('-', 3)
        dob_new.append(dob_old[1] + "/" + dob_old[2] + "/" + dob_old[0])

        #masking SSN
        ssn_old = row[3]
        ssn_old = ssn_old.split('-', 3)
        ssn_new.append("***-**-" + ssn_old[2])

        #using us_state_abbrev to change state name
        state_old = row[4]
        state_new.append(us_state_abbrev[state_old])


 
for x in range(len(state_new)):
    print (state_new[x])
print (len(state_new))