#Importing libraries
import os
import csv

#setting path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#variable initialization
month_count = 0 #initializes to 0 since data contains headers
total_profit = 0
initial_profit = 0
profit_delta = []
max_profit = 0
max_loss = 0

#opening budget_data.csv
with open(csvpath, newline='', encoding='UTF-8') as csvresults:
    csvreader = csv.reader(csvresults, delimiter=',')
    next(csvreader) #skipping the headers
    #for loop that will cycle through every row retrieving relevant data
    for month in csvreader:
        month_count += 1 #increases month_count
        total_profit += int(month[1]) #adds total profit
        final_profit = int(month[1]) - initial_profit
        initial_profit = int(month[1]) #sets the current profit as the initial profit for next iteration
        if month_count > 1: #can't calculate profit for 1st month, since there is no previous value   
            profit_delta.append(final_profit)
        #determining max profit/losses
        if final_profit > max_profit:
            max_profit = final_profit
            max_month = month[0]
        if final_profit < max_loss:
            max_loss = final_profit
            min_month = month[0]

#done with the csv results, can be closed now

#calculating the average profit/loss for each month

#variable initialization
sum_delta = 0

#for loop that will cycle through every month to add/substract it to the total profit
for delta in range(len(profit_delta)):
    sum_delta += profit_delta[delta]

average_profit = round(sum_delta / (len(profit_delta)),2) #rounding the average profit to 2 decimals to be consistent with currency data

#creating results.txt
with open("results.txt", "w") as results:
    results.write ("Financial Analysis \n")
    results.write ("------------------------\n")
    results.write ("Total months: " + str(month_count) + "\n")
    results.write ("Total: $" + str(total_profit) + "\n")
    results.write ("Average change: $" + str(average_profit) + "\n")
    results.write ("Greatest increase in profits: " + max_month + "($" + str(max_profit) + ")\n")
    results.write ("Greatest decrease in losses: " + min_month + "($" + str(max_loss) + ")\n")

#printing the results to the terminal
with open("results.txt", "r") as results:
    for line in results:
        print (line, end = " ")