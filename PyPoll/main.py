#importing libraries
import os
import csv

#path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#variable initialization
total_votes = 0 #initialized to 0 because data table has headers
candidate_list = []
votes_by_candidate = []

#opening the csv file
with open(csvpath, newline='', encoding='UTF-8') as csvresults:
    csvreader = csv.reader(csvresults, delimiter=',')
    next(csvreader) #skipping the headers
    #for loop that will cycle through every vote casted
    for vote in csvreader:
        total_votes += 1 #updating the total number of votes

        #searching for the candidate in the candidate_list

        #retrieving the candidate name
        candidate_name = vote[2]

        #resetting new_candidate variable
        new_candidate = True

        #checking if candidate is already in the list
        for candidate in range(len(candidate_list)):
            if candidate_name == candidate_list[candidate]:
                votes_by_candidate[candidate] +=1
                new_candidate = False
        
        #adding the candidate name if it is a new one
        if new_candidate == True:
            candidate_list.append(candidate_name)
            votes_by_candidate.append(1)
#done with the csv file, can close now

#calculating and creating the list with percentage of votes
percentage_by_candidate = []

#for loop that will cycle through every item in the votes by candidate list
for x in range(len(votes_by_candidate)):
    votes_percentage = round(100* (votes_by_candidate[x] / total_votes), 3) #rounds the percentage to 3 decimal places
    percentage_by_candidate.append(votes_percentage)    

#determining the winner of the election
winner_votes = 0
for x in range(len(votes_by_candidate)):
    if votes_by_candidate[x] > winner_votes:
        winner_votes = votes_by_candidate[x]
        winner_name = candidate_list[x]

#zipping the lists together for easier formatting in the results file
zipped_results = zip(candidate_list, percentage_by_candidate, votes_by_candidate)


#creating and formatting the txt file
with open("results.txt", "w") as results:
    results.write("Elections results \n")
    results.write("---------------------\n")
    results.write("Total votes: " + str(total_votes) + "\n")
    results.write("---------------------\n")
    for a, b, c in zipped_results:
        results.write(str(a) + ": " + str(b) + "%" + " (" + str(c) + ")\n")
    results.write("---------------------\n")
    results.write("Winner: " + winner_name + "\n")
    results.write("---------------------\n")

#printing the results to the terminal
with open("results.txt", "r") as results:
    for line in results:
        print (line, end = " ")

