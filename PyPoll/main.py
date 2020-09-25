#import your file
import csv
import os

#decalre your pathway
csvpath = os.path.join('.','Resources','election_data.csv')
csvpath_output = ('election_data.txt')

#add designated lists
votesCast = []
candidateVotes = []
names = []

#read the budget_data csv file 
with open(csvpath, newline = "") as myFile:
    csvreader = csv.reader(myFile, delimiter = ',') 
    csvHeader = next(myFile)
    
    for row in csvreader:
        votesCast.append(row[0])
        candidateVotes.append((row[2]))
        
        if row[2] not in names:
            names.append(row[2])

    def electionResults(candidateVotes):
        return max(set(candidateVotes), key = candidateVotes.count)

#return data for printing
    print('Election Results')
    print('----------')
    print('Total Number of Votes: {}'.format(len(votesCast)))
    print('----------')
    for candidate in names:
        print('{}: {:.3f}% ({})'.format(candidate,(candidateVotes.count(candidate)/len(votesCast))*100,candidateVotes.count(candidate)))
    print('----------')
    print('Winner: {}'.format(electionResults(candidateVotes)))

#export text file
output = os.path.join('.','Analysis','election_data_analysis.txt')

with open(output,"w", newline = "") as textFile:
    writer = csv.writer(textFile)
    textFile.write('Election Results')
    textFile.write('----------')
    textFile.write('Total Number of Votes: {}'.format(len(votesCast)))
    textFile.write('----------')
    for candidate in names:
        textFile.write('{}: {:.3f}% ({})'.format(candidate,(candidateVotes.count(candidate)/len(votesCast))*100,candidateVotes.count(candidate)))
    textFile.write('----------')
    textFile.write('Winner: {}'.format(electionResults(candidateVotes)))
