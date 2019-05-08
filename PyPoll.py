

# Dependencies
import os
import csv

csvpath = os.path.join(".", "desktop", "python-challenge","PyRoll",'election_data.csv')
# The total number of votes included in the dataset
total_votes_cast = []
candidate_list = []
percentage_vote = []
total_votes_won = []
popular_vote = []
# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
# CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

