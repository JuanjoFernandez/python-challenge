#Importing libraries
import os
import csv

#opening budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#variable initialization
month_count = 0 #initializes to 0 since data contains headers
total_profit = 0
initial_profit = 0
profit_delta = []

with open(csvpath, newline='', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) #skipping the headers
    #for loop that will cycle through every row retrieving relevant data
    for month in csvreader:
        month_count += 1 #increases month_count
        total_profit += int(month[1]) #adds total profit
        final_profit = int(month[1]) - initial_profit
        initial_profit = int(month[1]) #sets the current profit as the initial profit for next iteration
        if month_count > 1: #can't calculate profit for 1st month, since there is no previous value   
            profit_delta.append(final_profit)

#done with the csv file, can be closed now

#calculating the average profit/loss for each month

#variable initialization
sum_delta = 0

for delta in range(len(profit_delta)):
    sum_delta += profit_delta[delta]

average_profit = sum_delta / (len(profit_delta)+1) #adding 1 to the index since indexes start at 0

print (len(profit_delta))
print (average_profit)

