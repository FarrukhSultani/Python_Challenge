#Read csv file
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
month_counts = 0
total = 0
date=[]
difference = []
increase =['', 0]
decrease=['', 100000000000]
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    month_counts+=1
    total+=int(first_row[1])
    previous = int(first_row[1])

    for row in csvreader: 
        month_counts+=1
        total+=int(row[1])

        change = int(row[1])- previous
        previous = int(row[1]) 

        difference.append(change)
        date.append(row[0])

        if change > increase[1]:
            increase[1]=change
            increase[0] = row[0]

        if change < decrease[1]:
            decrease[1]=change
            decrease[0] = row[0]

average_change = sum(difference)/ len(difference)

result=(f"""
Financial Analysis
----------------------------
Total Months: {month_counts}
Total: ${total:,.2f}
Average Change: ${average_change:,.2f}
Greatest Increase in Profits: {increase[0]} (${increase[1]:,.2f})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]:,.2f})
""")
print(result)
output_path = os.path.join("Analysis","budget_analysis.txt")
with open(output_path,"w") as file:
    file.write(result)
