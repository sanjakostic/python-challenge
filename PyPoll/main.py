import os
import csv

# generate file path for input file
file_path = os.path.join(".","Resources","election_data.csv")

full_data = list()

# open the input file, and for each row of text in csvreader,
# append the line of text to list full_data
with open(file_path, encoding='utf-8') as csvf:
    csvreader =  csv.reader(csvf, delimiter=",")
    for i in csvreader:
        full_data.append(i)

# separate the header (header) from the rest of the data (full_data)
header = full_data[0]
full_data = full_data[1:]

# total_votes is the total number of votes, equal to the length of the data full_data
total_votes = len(full_data)

candidate_votes = dict()

# for each row (i) in full_data, i[2] is the candidate's name
for i in full_data:
    # if the candidate is not yet in the dictionary as a key, 
    # add that candidate with initial value (vote count) 1
    if i[2] not in candidate_votes.keys():
        candidate_votes[i[2]] = 1
    # if the candidate is already in the keys, then 
    # increment their count by one
    else:
        candidate_votes[i[2]] += 1

candidate_percentages = dict()

# create a dictionary called candidate_percentages that takes
# candidate_votes, and divides by the total number of votes
# and multiplies by 100 to get the percentage as a dictionary
# with the same keys
for i in candidate_votes.items():
    candidate_percentages[i[0]] = (candidate_votes[i[0]] / total_votes) *100

# The winner is going to be the candidate with the highest (max)
# percentage of votes
winner = max(candidate_percentages, key=candidate_percentages.get)

# generate output file path
outfile_path = os.path.join(".","analysis","pypoll_analysis.txt")

# output file procedure
outfile = open(outfile_path, 'w')

outfile.write("Election Results\n")
outfile.write("-------------------------\n")
outfile.write(f"Total Votes: {total_votes}\n")
outfile.write(f"-------------------------\n")
# in this for loop, the keys for candidate_votes and candidate_percentages
# are the same set of keys. So, getting the key for one should map to 
# the keys for the other. This way, we get both the candidate's votes
# and percentages in one line
for i in candidate_votes.items():
    outfile.write(f'{i[0]}: {round(candidate_percentages[i[0]],3)}% ({i[1]})\n')
outfile.write(f"-------------------------\n")
outfile.write(f"Winner: {winner}\n")
outfile.write("-------------------------\n")

outfile.close()
