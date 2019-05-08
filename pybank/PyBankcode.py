import os
import csv
csvpath = os.path.join(".", "desktop", "python-challenge","pybank",'budget_data.csv')
# The total number of months included in the dataset
total_months = []
monthly_change = []
net_amount = [ ]

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
# CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
   
# Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    for row in csv.reader(csvfile):
        total_months.append(row[0])
        net_amount.append(int(row[1]))
    print(f"CSV Header: {csv_header}")

    for a in range(len(net_amount) -1):
        monthly_change.append(net_amount[a+1] - net_amount[a])
     
    Increase_max_change = max(monthly_change)
    Decrease_max_change = min(monthly_change)
     
    print(f'Financial Analysis')
    print('----------------------------------------------------------------------------')
    print(f"Total Months: {len(total_months)}")
    print(f"Net Profit: {sum(net_amount)}")
    print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
    print(f"Greatest Increase in Profits: ${str(max(monthly_change))}")
    print(f"Greatest Decrease in Profits: ${str(min(monthly_change))}")

# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join(".", "desktop", "python-challenge","pybank", 'Financial Analysis1.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 
    'Net Profit', 
    'Average Change', 
    'Greatest Increase in Profits', 
    'Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerow([len(total_months), 
    sum(net_amount), 
    round(sum(monthly_change)/len(monthly_change),2), 
    (max(monthly_change)), 
    (min(monthly_change))])

csvwriter.writerow['Total Months'] = 'len(total_months)'
    
