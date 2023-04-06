import os
import csv
print("Election Results")
print("------------------")
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    Total_Votes = 0
    for row in csvfile:
        Total_Votes += 1
    print("Total Votes:", Total_Votes)

print("------------------")

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    candidates = [] 
    for row in csvfile: 
        if row[2] in candidates: 
            candidates.append(row[2])
        else: 
            continue 
