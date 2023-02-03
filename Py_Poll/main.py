#Read the CSV file
import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
output = open('Analysis/Election_result.txt', 'w')
print(csvpath)
#Define variables
votecounts = 0
county = []
candidates_name = []
wincounts = {}
winpercent = 0
totalvotecounts= 0
winnername = ''
winnervotecounts = 0

#The total number of votes cast
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header:{csv_header}")
    output.write(f"Header:{csv_header}\n")
# The total number of votes each candidate won
    for row in csvreader:
        votecounts += 1
        totalvotecounts += 1
        county = row[1]
        candidate = row[2]
#complete list of candidates 
        if candidate not in candidates_name:
            candidates_name.append(candidate)
            wincounts[candidate] = 0
        wincounts[candidate] += 1

#Print result
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {totalvotecounts}")
print(f"-------------------------")
output.write(f"Election Results\n")
output.write(f"-------------------------\n")
output.write(f"Total Votes: {totalvotecounts}\n")
output.write(f"-------------------------\n")

# The percentage of votes each candidate won/winpercent
for candidate in wincounts:
    votes = wincounts[candidate]
    winpercent = votes/totalvotecounts
    pretty_percent = winpercent * 100
    print(f"{candidate}: {pretty_percent:.3f}%({votes})")
    output.write(f"{candidate}: {pretty_percent:.3f}%({votes})\n")

# The winner of the election based on popular vote
for candidate in wincounts:
    if wincounts[candidate] > winnervotecounts:
        winnervotecounts = wincounts[candidate]
        winner_name = candidate

print(f"----------------------------------------")
print(f"Winner: {winner_name}")
print(f"----------------------------------------")
output.write(f"----------------------------------------\n")
output.write(f"Winner: {winner_name}\n")
output.write(f"----------------------------------------\n")
