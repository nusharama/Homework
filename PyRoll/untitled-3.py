import csv
import os

csvpath = os.path.join(".", "desktop", "python-challenge", "PyRoll", 'election_data.csv')
# The total number of votes included in the dataset
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

khan_percent = 0
correy_percent = 0
li_percent = 0
otooley_percent = 0


# Open & Read CSV File
with open(csvpath, newline='') as csvfile:

    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

# Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    for row in csv.reader(csvfile):
        total_votes += 1
        if (row[2]) == "Khan":
            khan_votes += 1
        elif(row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
    else:
        otooley_votes += 1
    print(f"CSV Header: {csv_header}")

khan_percent = khan_votes / total_votes
correy_percent = correy_votes / total_votes
li_percent = li_votes / total_votes
otooley_percent = otooley_votes / total_votes

winner = max(khan_votes, correy_votes, li_votes,otooley_votes)

if winner == khan_votes:
        winner_name = "khan"
elif winner == correy_votes:
        winner_name = "correy"
elif winner_name == li_votes:
        winner_name = "li"

print(f'Election Results')
print('----------------------------------------------------------------------------')
print(f"Total Votes: {(total_votes)}")
print('----------------------------------------------------------------------------')
print(f"Khan: {(khan_votes)}")
print(f"Correy: {(correy_votes)}")
print(f"Li: {((li_votes))}")
print(f"O'Tooley: {((otooley_votes))}")
print('----------------------------------------------------------------------------')
