import csv
import os

csvpath = os.path.join(".", "desktop", "python-challenge", "PyRoll", 'election_data.csv')
# The total number of votes included in the dataset
poll = {}
total_votes = 0 
candidates = []
num_votes = []


# Open & Read CSV File
with open(csvpath, newline='') as csvfile:

    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

# Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csv.reader(csvfile):
        total_votes += 1
    if (row[2] in poll.keys()
        poll [row[2]] = poll[row[2]] + 1
    else: 
        poll[row[2]] = 1
        

    for key.value in poll items()
        candidates.append(key)
        num_votes.append(value)

        


    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "khan"
    elif winner == correy_votes:
        winner_name = "correy"
    elif winner_name == li_votes:
        winner_name = "li"

    




print(f'Election Results')
print('----------------------------------------------------------------------------')
print(f"Total Votes: {()}")
print('----------------------------------------------------------------------------')
print(f"Khan: {()}")
print(f"Correy: ${(()/())}")
print(f"Li: ${(())}")
print(f"O'Tooley: ${(())}")
print('----------------------------------------------------------------------------')
