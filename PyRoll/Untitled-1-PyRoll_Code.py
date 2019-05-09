import os
import csv
csvpath = os.path.join(".", "desktop", "python-challenge","PyRoll",'election_data.csv')

# The total number of votes included in the dataset
total_votes_cast = 0
total_votes = 0
candidate_votes = 0
candidate_list = 0
number_candidates = 0
percentage_vote = 0
total_votes_won = 0
winner = 0

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
        total_votes_cast.append(row[1])
        total_votes.append(row[1])
        total_votes = total_votes + 1
        print(f"{len(int(total_votes_cast))}")
 
# Set the candidate names to candidatelist
candidate_list = row [0]
if candidate_list not in candidate_list:
    number_candidates = number_candidates + 1
candidate_list.append(candidate_list)
candidate_votes[candidate_list] = 0

candidate_votes[candidate_list] = candidate_votes[candidate_list] + 1
      
print(f'Election Results')
print('----------------------------------------------------------------------------')
print(f"Total Votes: {()}")
print('----------------------------------------------------------------------------')
print(f"Khan: {()}")
print(f"Correy: ${(()/())}")
print(f"Li: ${(())}")
print(f"O'Tooley: ${(())}")
print('----------------------------------------------------------------------------')
        