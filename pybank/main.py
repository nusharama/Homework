import os
import csv

csvpath = os.path.join(".", "pybank",'budget_data.csv')
# csvpath = os.path.join ("C:\Users\anoos\Desktop\python-challenge\pybank\'budget_data.csv')
# The total number of months included in the dataset
total_months = 0
monthly_change = []
net_amount = []
month_increase = ''
month_decrease = ''
date = []
# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
# CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # print(csvreader)
   
# Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    
    for row in csv.reader(csvfile):
        total_months = total_months+1
        # total_months.append(row[0])
        net_amount.append(int(row[1]))
        date.append(row[0])
    # print(f"CSV Header: {csv_header}")

    for a in range(1, len(net_amount)):
        monthly_change.append(net_amount[a]-net_amount[a-1])
        
        Increase_max_change = max(monthly_change)
        Decrease_max_change = min(monthly_change)
        if (net_amount[a]-net_amount[a-1]) == (Increase_max_change):
            month_increase = (row[0])
        if (net_amount[a]-net_amount[a-1]) == (Decrease_max_change):
            month_decrease = (row[0])

date.pop(0)
max_position = (monthly_change.index(max(monthly_change)))
min_position = (monthly_change.index(min(monthly_change)))    
         
print(f'Financial Analysis')
print('----------------------------------------------------------------------------')
print(f"Total Months: {(total_months)}")
print(f"Net Profit: ${(sum(net_amount))}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {date[max_position]} ${str(max(monthly_change))}")
print(f"Greatest Decrease in Profits: {date[min_position]} ${str(min(monthly_change))}")
# print(monthly_change.index(max(monthly_change)))
# print(monthly_change.index(min(monthly_change)))


# Specify the file to write to
# output_path = os.path.join(".", "pybank", 'FinancialAnalysis.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    # csvwriter = csv.writer(csvfile, delimiter=',')

    # # Write the first row (column headers)
    # csvwriter.writerow(['Total Months', 
    # 'Net Profit', 
    # 'Average Change', 
    # 'Month Increase', 'Month decrease',
    # 'Greatest Increase in Profits', 
    # 'Greatest Decrease in Profits'])

    # # Write the second row
    # csvwriter.writerow([(total_months), 
    # sum(net_amount), 
    # round(sum(monthly_change)/len(monthly_change),2), 
    # (date[max_position]), (date[min_position]), 
    # (max(monthly_change)), 
    # (min(monthly_change))])

with open('Pybank\Financial Analysis.txt', 'w') as outfile:
    print(f'Financial Analysis', file=outfile)
    print('----------------------------------------------------------------------------')
    print(f"Total Months: {(total_months)}", file=outfile)
    print(f"Net Profit: ${(sum(net_amount))}", file=outfile)
    print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}", file=outfile)
    print(f"Greatest Increase in Profits: {date[max_position]} ${str(max(monthly_change))}", file=outfile)
    print(f"Greatest Decrease in Profits: {date[min_position]} ${str(min(monthly_change))}", file=outfile)
    
