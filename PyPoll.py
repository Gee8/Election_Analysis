# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total nuber of votes each candidate won
# 5. The winner of the election based on popular vote

#add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter and candidate lists and candidate dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

#Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # read headers of the CSV file.
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #increase total votes
        total_votes += 1
        #puts all names in candidate_name
        candidate_name = row[2]
        #adds unique names to candidate_options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #create each candidate as a key
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#iterate through candidate list to retrieve vote counts of each candidate and percent of vote
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote')

    # print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent =
        #vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)









