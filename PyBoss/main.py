#Importing libraries
import os
import csv
from us_state_abbrev import us_state_abbrev

#setting ths csv path
csvpath = os.path.join('Resources', 'employee_data.csv')

#variable initialization
employee_id = []
first_name = []
last_name = []
dob_new = []
ssn_new = []
state_new = []

#opening the csv file
with open(csvpath, newline='', encoding='UTF-8') as csvdata:
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
#done with the csv file, can close now

#creating the new csv file
csvpath = os.path.join ('Resources', 'employee_data_new.csv')

with open(csvpath, 'w', newline='', encoding='UTF-8') as csvdata:
    csvwriter = csv.writer(csvdata, delimiter=',')

    #Creating the headers
    headers = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
    csvwriter.writerow(headers)
    
    #for loop that will create each row for the new file
    for row in range(len(employee_id)):
        row = [employee_id[row],
                first_name[row],
                last_name[row],
                dob_new[row],
                ssn_new[row],
                state_new[row]]
        csvwriter.writerow(row)