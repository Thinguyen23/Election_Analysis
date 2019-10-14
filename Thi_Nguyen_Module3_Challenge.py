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
candidate_votes={}

# Declare winning candidate and winning count tracker
winning_candidate=''
winning_count=0
winning_percentage=0

# CHALLENGE
# Declare list of counties and empty dictionary for each county's vote
counties=[]
county_votes={}
# Declare county that has the largest turnout and number of votes
largest_turnout_county=''
largest_votes=0

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

        # Get the county from each row
        county=row[1]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # CHALLENGE
        if county not in counties:
            # Add the county name to counties list
            counties.append(county)
            # Begin tracking vote for each county
            county_votes[county]=0
        # Add a vote to that county
        county_votes[county]+=1


# Save results to text file
with open(file_to_save,'w') as txt_file:
    # Print final count to terminal
    election_results=(
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
    print(election_results,end='')
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # CHALLENGE
    # County Vote header
    print(f'\nCounty Votes:\n')
    txt_file.write(f'\nCounty Votes:\n')
    # Determine the percentage of votes for each county by looping through counts
    for county in county_votes:
        # Vote count for each county
        votes=county_votes[county]
        # Percentage of votes for each county
        vote_percent=int(votes)/int(total_votes)*100
        # Print county name and results to terminal and save to text file
        county_results=(f'{county}: {vote_percent: .1f}% ({votes:,}).\n')
        print(county_results)
        txt_file.write(county_results)

        # Determne county with the largest turnout votes
        if (votes>largest_votes):
            largest_votes=votes
            largest_turnout_county=county
    
    # Print out Largest County Turnout
    largest_turnout=(
        f'\n-------------------------\n'
        f'Largest County Turnout: {largest_turnout_county}\n'
        f'-------------------------\n')
    print(largest_turnout)
    txt_file.write(largest_turnout)
    #----------- END CHALLENGE

    
    # Determine the percentage of votes for each candidate by looping through the counts
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes=candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage=int(votes)/int(total_votes)*100
        # Candidate name and percentage of votes
        candidate_results= (f'{candidate}: {vote_percentage:.1f}% ({votes:,}).\n')
        # print each candidate vote count and percentage to terminal
        print(candidate_results)
        # Save to election analysis text file
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        # Determine if the votes is greater then the winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            # If true, set winning_count, winning_percentage and winning candidate
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate

    # Print out winning candidate summary
    winning_candidate_summary=(
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning vote count: {winning_count:,}\n'
        f'Winning percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print(winning_candidate_summary)
    # Save to election analysis text file
    txt_file.write(winning_candidate_summary)




        



