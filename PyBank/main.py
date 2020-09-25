#import your file
import csv
import os

#decalre your pathway
csvpath = os.path.join('.','Resources','budget_data.csv')
csvpath_output = ('budget_data.txt')

#add designated lists
totalMonths = []
profit = []
monthDate = []
profitDelta = []

#read the budget_data csv file 
with open(csvpath, newline = "") as myFile:
    csvreader = csv.reader(myFile, delimiter = ',') 
    csvHeader = next(myFile)
    
    for row in csvreader:
        totalMonths.append(row[0])
        profit.append(int(row[1]))
        net = sum(profit)
        monthDate.append(row[0])
        greatestIncrease = profit.index(max(profit))
        greatestDecrease = profit.index(min(profit))
    
    for rows in range(len(profit)-1):
        profitDelta.append(profit[rows+1]-profit[rows])

#return data for printing
    print('Financial Analysis')
    print('\n')
    print('----------')
    print('\n')
    print('Total Months: {}'.format(len(totalMonths)))
    print('\n')
    print('Net Profit: ${}'.format(net))
    print('\n')
    print('Average Change: {}'.format(round(sum(profitDelta)/len(profitDelta),2)))
    print('\n')
    print('Greatest Increase: {} (${})'.format((monthDate[greatestIncrease]),(max(profitDelta))))
    print('\n')
    print('Greatest Decrease: {} (${})'.format((monthDate[greatestDecrease]),(min(profitDelta))))

#export text file
output = os.path.join('.','Analysis','budget_data_analysis.txt')

with open(output,"w", newline = "") as textFile:
    writer = csv.writer(textFile)
    textFile.write('Financial Analysis')
    textFile.write('\n')
    textFile.write('----------')
    textFile.write('\n')
    textFile.write('Total Months: {}'.format(len(totalMonths)))
    textFile.write('\n')
    textFile.write('Net Profit: ${}'.format(net))
    textFile.write('\n')
    textFile.write('Average Change: {}'.format(round(sum(profitDelta)/len(profitDelta),2)))
    textFile.write('\n')
    textFile.write('Greatest Increase: {} (${})'.format((monthDate[greatestIncrease]),(max(profitDelta))))
    textFile.write('\n')
    textFile.write('Greatest Decrease: {} (${})'.format((monthDate[greatestDecrease]),(min(profitDelta))))
    
