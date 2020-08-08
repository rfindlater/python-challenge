# In this challenge, you are tasked with helping a small, 
# rural town modernize its vote-counting process.

# import dependencies
import os
import csv
import statistics


# create path for reading data
bd_csv = os.path.join('..','Resources', 'election_data.csv')

# variables

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


#Open and read csv
with open(bd_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    
    csv_header = next(csvreader)

# * The total number of votes cast
    for row in csvreader:
        total_votes += 1


#   * A complete list of candidates who received votes
#   * The total number of votes each candidate won
    # for row2 in csvreader:
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1    
#   * The percentage of votes each candidate won
khan_percentage = (khan_votes/total_votes)  * 100
correy_percentage = (correy_votes/total_votes) * 100
li_percentage = (li_votes/total_votes) * 100
otooley_percentage = (otooley_votes/total_votes) * 100

# set variables for determining winner
vote_max = khan_votes
winner = "Khan"
# if statements to determine winner
if correy_votes > vote_max:
    vote_max = correy_votes
    winner = "Correy"
if li_votes > vote_max:
    vote_max = li_votes
    winner = "Li"
if otooley_votes > vote_max:
    vote_max = otooley_votes
    winner = "O'Tooley"


#   * The winner of the election based on popular vote.
print(otooley_votes)
print(f"Election Results")
print("----------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------------------------")
print(f"Khan: {khan_percentage:.3f}% ({str(khan_votes)})")
print(f"Correy: {correy_percentage:.3f}% ({correy_votes})")
print(f"Li: {li_percentage:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percentage:.3f}% ({otooley_votes})")
print("----------------------------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------------------------")
# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```