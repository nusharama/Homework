import csv
import os

csvpath = os.path.join(".", "desktop", "python-challenge", "PyRoll", 'election_data.csv')
# The total number of votes included in the dataset
poll = {}
total_votes = 0
file_num = 1

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:

    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    for row in csv.reader(csvfile):
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#create empty list for candidates and his/her vote count
candidates = []
num_votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

print(f'Election Results')
print('----------------------------------------------------------------------------')
print(f"Total Votes: {(total_votes)}")
print('----------------------------------------------------------------------------')
