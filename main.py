#PyBank, main.py
#print to terminal and with a *.txt file
#Total Months, Total, Average Change, Greatest Increase in Profits, Greatest Decrease in Profits

#importing os and csv modules
import os
import csv

#import "Resources/budget_data.csv", same structure for GitHub
csvpath = os.path.join('Resources','budget_data.csv')

#test csvpath accuracy
#print(csvpath)
#verified correct

cwd = os.getcwd()

print(cwd)

#Read CSV
# with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')

#     print(csvreader)

#     # Read the header row first (skip this step if there is now header)
#     csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")

#     # Read each row of data after the header
#     for row in csvreader:
#         print(row)

        

#print(len(csvreader)-1)
#print("test")
