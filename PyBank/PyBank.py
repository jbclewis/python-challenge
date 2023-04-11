import os
import csv
import sys

csvpath = os.path.join('Resources', 'budget_data.csv') 
os.chdir(os.path.dirname(os.path.realpath(__file__))) 

total_months = 0
total_money = 0
previous_profit = None 
max = 0 
min = 0 
total_change = 0 

with open(csvpath) as csvfile: 
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        # counting the total number of months 
        total_months += 1
        current_profit = int(row['Profit/Losses'])
        # counting the total amount of Profit/Losses 
        total_money += current_profit 

        # skip the first month's Profit/Losses to then find the first profit change and each one after that
        if previous_profit is not None: 
            profit_change = current_profit - previous_profit 
            # counting the total of the changes to be able to then find the average change over the 86 months 
            total_change += profit_change
            average_change = str(round((total_change / (total_months - 1)), 2))
            # finding the greatest increase and decrease in Profits/Losses and the month that corresponds 
            if profit_change > max: 
                current_month_max = str(row['Date'])
                max = profit_change 
            if profit_change < min: 
                current_month_min = str(row['Date'])
                min = profit_change

        # prepare for next time 
        previous_profit = current_profit 
        
output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_money}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {current_month_max} ${max}\n" 
    f"Greatest Decrease in Profits: {current_month_min} ${min}\n"
)
print(output)

sourceFile = open('PyBank.txt', 'w')
print(output, file = sourceFile)
sourceFile.close()
original_stdout = sys.stdout 	
