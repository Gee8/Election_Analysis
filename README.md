# Election_Analysis
## Overview of Election Audit:
The purpose of the election audit analysis was to read the raw election data from a csv file, and be able to return an analysis printed to the terminal and written to a text file named election_analysis.txt. From the csv file, we were able to determine total votes, county votes and percentages, the largest county turnout, the candidates total votes and percentages, and the winner of the election with the number of votes and percentage of votes.

## Election-Audit Results:

- How many votes were cast in this congressional election?
  - There were a total of 369,711 votes cast in this congressional election.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Jefferson had 38,855 or 10.5% of the total votes. Denver had 306,055 or 82.8% of the total votes. Arapahoe had 24,801 or 6.7% of the total votes.

- Which county had the largest number of votes?
  - The county with the largest number of votes was Denver with 306,055 votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Caster Stockham recieved 85,213 or 23% of the total votes. Diana DeGette recieved 272,892 or 73.8% of the total votes. Raymon Anthony Doane recieved 11,606 or 3.2% of the total votes.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana DeGette won the election with 272,892 votes. She recieved 73.8% of the total votes.

Shown below is a screenshot of the election results written to election_analysis.txt.

<img width="300" alt="Election_Results" src=".\Resources\Election_Results.png">

## Election-Audit Summary:
For any given election, our PyPoll_Challenge.py script should be able to be used to generate the election outcomes. If the data collected for a future election was in the same format as our election_results.csv, the only thing we have to change would be the file we are reading, for example we used: `file_to_load = os.path.join("Resources", "election_results.csv")`. If the data within the new csv file was structured differently, we could change where we pull the data from. For example, `candidate_name = row[2]` and `county = row[1]` can be adjusted to pull a different category from the column within the new data set. If the next election data came from a national level, we could use the same approach and look at states instead of counties.