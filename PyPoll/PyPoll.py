import os
import csv
import sys

csvpath = os.path.join('Resources', 'election_data.csv') 
os.chdir(os.path.dirname(os.path.realpath(__file__))) 

# starting with an empty list for the candidates 
candidate_list = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # store the header row 
    csvheader = next(csvreader)
    # count the total number of votes, equivalent to the number of rows 
    total_votes = 0
    for row in csvreader:
        total_votes += 1
        # go through the rows and keep track of each candidate's votes 
        candidate = row[2]
        if candidate in candidate_list:
            candidate_list[candidate] += 1
        else:
            candidate_list[candidate] = 1

    # find the candidate with the most votes 
    most_votes = 0
    winner = ""
    for candidate in candidate_list:
        if candidate_list[candidate] > most_votes:
            most_votes = candidate_list[candidate]
            winner = candidate 

output = f"Election Results\n" \
    f"------------------\n" \
    f"Total Votes: {total_votes}\n" \
    f"------------------\n"
for candidate in candidate_list:
    candidate_percent = round(candidate_list[candidate] * 100 / total_votes, 3)
    output += f"{candidate}: {candidate_percent}% ({candidate_list[candidate]})\n" 
output += f"Winner: {winner}\n"
print(output)

sourceFile = open('PyPoll.txt', 'w')
print(output, file = sourceFile)
sourceFile.close()
original_stdout = sys.stdout 	
