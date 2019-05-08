import os
import csv
csvpath = os.path.join(".", "desktop", "python-challenge","PyRoll",'election_data.csv')

# The total number of votes included in the dataset
total_votes_cast = []
candidate_list = []
percentage_vote = []
total_votes_won = []
popular_vote = []

khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
# CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # print(f"CSV Header: {csv_header}")
 # The total number of votes cast
# Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    for row in csv.reader(csvfile):
        total_votes_cast.append(row[0])
        total_votes = total_votes + 1
print(f"{len(int(total_votes_cast))}")
 
# Set the candidate names to candidatelist
candidate_list.append(row[2])

        If(row [2] == "Khan"):
            khan_votes = khan_votes + 1

    

print(f'Financial Analysis')
    print('----------------------------------------------------------------------------')
    print(f"Total Months: {len(total_months)}")
    print(f"Net Profit: {sum(net_amount)}")
    print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
    print(f"Greatest Increase in Profits: ${str(max(monthly_change))}")
    print(f"Greatest Decrease in Profits: ${str(min(monthly_change))}")
