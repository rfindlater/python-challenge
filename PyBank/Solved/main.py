# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv
import statistics

bd_csv = os.path.join('../Resources', 'budget_data.csv')

#holders for data
months=[]
profitsLoss=[]

# Define function and have it accept 'budget_data'

#variables
count = 0
totalProfitLosses = 0
total_months = 0
greatest_increase = ["",0]
greatest_decrease = ["",9999999999]


#Open and read csv
with open(bd_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    
    csv_header = next(csvreader)
    
    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = int(first_row[1])
    previous_net = total_net
# loop through data to count total months and calculate net change for profits loss
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1]) 

# append profits loss 

        profitsLoss.append(total_net) 

        if net_change > greatest_increase[1]: 
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(profitsLoss) / len(profitsLoss)

#   In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# print("```text")
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {total_months}") 
print(f"Total Profits: ${total_net}")
print(f"Average  Change: ${net_monthly_avg}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
