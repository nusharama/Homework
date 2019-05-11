import csv
import os

csvpath = os.path.join(".", "PyRoll", 'election_data.csv')

# The total number of votes included in the dataset
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

percentage = []
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
         # Calculate Total Number Of Votes Cast
        total_votes += 1
        
# Calculate Total Number Of Votes Each Candidate Won
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
# Calculate Percentage Of Votes Each Candidate Won
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

        
# Calculate Winner Of The Election Based On Popular Vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {khan_percent:.3%} ({khan_votes})")
print(f"Correy: {correy_percent:.3%} ({correy_votes})")
print(f"Li: {li_percent:.3%} ({li_votes})")
print(f"OTooley: {otooley_percent:.3%} ({otooley_votes})")
print(f"---------------------------")
print(f"Winner:{winner_name}")
print(f"---------------------------")

# Dependencies
import os
import csv

# Specify the file to write to
# output_path = os.path.join(".", "desktop", "python-challenge","PyRoll", 'Election_Results.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

# Initialize csv.writer
    # csvwriter = csv.writer(csvfile, delimiter=',', )
# Write the second row

with open('PyRoll\Election Results.txt', 'w') as outfile:
    print(f"Election Results", file=outfile)
    print(f"---------------------------", file=outfile)
    print(f"Total Votes: {total_votes}", file=outfile)
    print("---------------------------", file=outfile)
    print(f"Khan: {khan_percent:.3%} ({khan_votes})", file=outfile)
    print(f"Correy: {correy_percent:.3%} ({correy_votes})", file=outfile) 
    print(f"Li: {li_percent:.3%} ({li_votes})", file=outfile) 
    print(f"O'Tooley: {otooley_percent:.3%} ({otooley_votes})", file=outfile)
    print("---------------------------", file=outfile)
    print(f" Winner: {winner_name}", file=outfile)
    print("---------------------------", file=outfile)

    


