import os
import csv
print("Financial Analysis")
print("------------------")
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    Total_Months = 0
    for row in csvfile:
        Total_Months += 1
    print("Total Months:", Total_Months - 1)

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    Total_Money = 0
    for row in csvreader:
        Total_Money += int(row['Profit/Losses'])
    print("Total: $", Total_Money) 

Average_Money = 0 
#Average_Change = 
#print("Average_Change:", Average_Change) 

#with open(csvpath) as csvfile:
    #csvreader = csv.DictReader(csvfile, delimiter=',')
    #for row in csvreader: 
        #previous_month = int(row[1])
        #current_month = int(row[2])
#print(previous_month) 
#print(current_month)

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    max = 0
    for row in csvreader:
        if int(row['Profit/Losses'])>max:
            max = int(row['Profit/Losses'])
print("Greatest Increase in Profit:", max)

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    min = 0
    for row in csvreader:
        if int(row['Profit/Losses'])<min:
            min = int(row['Profit/Losses'])
print("Greatest Decrease in Profit:", min)
