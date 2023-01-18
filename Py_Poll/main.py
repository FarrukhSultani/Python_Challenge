#Read the CSV file
import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

#read headers
    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')
    # for row in csvreader:
    #     print(row)
    # #printing headers
    #     print(f'CSV Header: {csv_header}')
    #     print('Header:{csv_header}')
    #     print('Election Results')
    #     print('Charles Casper Stockham: ')
    #     print('Diana DeGette: ')
    #     print('Raymon Anthony Doane: ')
    #     print('Winner: ')

    #Define variables
    candidates_name = []
    wincounts = {}
    winpercent = 0
    winnername = ''
    winnervotecounts = 0
    votecounts = 0
    totalvotecounts= 0

    #The total number of votes cast
    for row in csvreader:
        votecounts +=1
    #A complete list of candidates who received votes
    candidates_name = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
    print (candidates_name)

    #The percentage of votes each candidate won
    for name in wincounts:
        votecounts = wincounts[name]
        winpercent = totalvotecounts / votecounts *100
        print(f"{name}: {winpercent} ({votecounts})")
    #The total number of votes each candidate won
        if name in candidates_name:
            candidates_name.append(row[2])
            wincounts[row[2]]=0
            wincounts[row[2]]+=1
    #The winner of the election based on popular vote
        if votecounts > winnervotecounts: 
            winnervotecounts = votecounts
            winnername = name
        print(f"{name}: {winpercent} ({votecounts})")
    