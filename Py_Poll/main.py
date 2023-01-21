#Read the CSV file
import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
output = open('Analysis/Election_result.txt')
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
    first_row = next(csvreader)
    votecounts+=1
    totalvotecounts+=int(first_row[0])
    previous = int(first_row[1])

 
 # A complete list of candidates who received votes
    candidates_name = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
    print(candidates_name)

# The total number of votes each candidate won
    for row in csvreader:
        if row[2] not in candidates_name:
            candidates_name.append(row[2])
            wincounts[row[2]]=0
            wincounts[row[2]]+=1

#Print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votecounts}")
print(f"-------------------------")
output.write(f"Election Results\n")
output.write(f"-------------------------\n")
output.write(f"Total Votes: {votecounts}\n")
output.write(f"-------------------------\n")

# The percentage of votes each candidate won
for  candidates_name in wincounts:
    votes = wincounts[candidates_name]
    winpercent = votes/votecounts
    pretty = winpercent * 100
    print(f"{candidates_name}: {pretty:.f}%({votes})")
output.write(f"{candidates_name}:{pretty:.3f}%({votes})\n")

# The winner of the election based on popular vote
if votes > winnervotecounts: 
    winnervotecounts = votes
    winnername = candidates_name

print(f"----------------------------------------")
print(f"Winner: {winnername}")
print(f"----------------------------------------")
output.write(f"-------------------------\n")
output.write(f"Winner: {winnername}\n")
output.write(f"-------------------------\n")
