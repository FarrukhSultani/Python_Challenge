#Read csv file
import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
#read headers
    csv_header = next(csvheader)
    print(f'CSV Header: {csv_header}')
for row in csvreader:
         print(row)

#printing headers
    print(f'CSV Header: {csv_header}')
    print('Header:{csv_header}')
    print('Financial Analysis')
    print('Total Months: ')
    print('Total: ')
    print('Average Change: ')
    print('Greatest Increase in Profits: ')
    print('Greatest Decrease in Profits: ' )

#defining variables
Total_months = month_counts
month_counts = 0
Total = (Average(Total))
Total = 0
Average_Change = 0
date=[]
profit = []
previous_profit = 0
difference = []
total_difference = 0
loss = 0
increase =('month': '','profit':0)
decrease=('month': '','profit/loss':0)

#The total number of months included in the dataset
for row in csvreader:
    print(row)
    Total_months = month_counts
    month_counts = 0
    Total_months = int(month_counts+1)

#The net total amount of "Profit/Losses" over the entire period
for row in csvreader:
        date.append(row[0])
        profit = int(row[1])
        profit/loss.append(profit)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
difference=0
for changes in profit:
    if previous_profit = 0 then
    difference = profit-previous_profit
    difference.append()
previous_profit = profit
    #average of the changes
def average(changes in profit)
    difference = profit-previous_profit
    total_difference = 0
    average(total_difference - difference/Total_months)
   
#The greatest increase in profits (date and amount) over the entire period
if difference > increase['profit']
    increase['profit'] = difference
    increase ['month'] = row.append(row[0])
#The greatest decrease in profits (date and amount) over the entire period
if difference < decrease['loss']
    decrease['loss'] = difference
    decrease ['month'] = row.append(row[0])
#Average of changes
 Average_Change = sum(total_difference) / int(Total_months)

