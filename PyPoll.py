# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes wach candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import os
import csv
# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources\election_results.csv')

# Assign a variable to load a file from a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes=0

#Candidate options and candidate votes
candidate_options=[]
# Declare the empty dictionary
candidate_votes={}
# Declare winning candidate and winning count tracker
winning_candidate=''
winning_count=0
winning_percentage=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    # Read the header row
    headers=next(file_reader)
    
    # Print each row
    for row in file_reader:
        # Add to the total vote count
        total_votes+=1

        # Print the candidate name from each row
        candidate_name=row[2]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote caount
            candidate_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through thr candidate list
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes=candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage=int(votes)/int(total_votes)*100
        # Print candidate name and percentage of votes
        print(f'{candidate}: {vote_percentage:.1f}% ({votes:,}).\n')

        #Determine winning vote count and candidate
        # Determine if the votes is greater then the winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            # If true, set winning_count, winning_percentage and winning candidate
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate

    # Print out winning candidate summary
    winning_candidate_summary=(
        f'-------------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning vote count: {winning_count:,}\n'
        f'Winning percentage: {winning_percentage:.1f}%\n'
        f'--------------------------------\n')
    print(winning_candidate_summary)
        




