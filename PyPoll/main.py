import os
import csv

file_path = os.path.join(".","Resources","election_data.csv")

full_data = list()

with open(file_path, encoding='utf-8') as csvf:
    csvreader =  csv.reader(csvf, delimiter=",")
    for i in csvreader:
        full_data.append(i)

header = full_data[0]
full_data = full_data[1:]

total_votes = len(full_data)

candidate_votes = dict()

for i in full_data:
    if i[2] not in candidate_votes.keys():
        candidate_votes[i[2]] = 1
    else:
        candidate_votes[i[2]] += 1

candidate_votes['Charles Casper Stockham']

candidate_percentages = dict()

for i in candidate_votes.items():
    candidate_percentages[i[0]] = (candidate_votes[i[0]] / total_votes) *100

winner = max(candidate_percentages, key=candidate_percentages.get)

outfile_path = os.path.join(".","analysis","pypoll_analysis.txt")

outfile = open(outfile_path, 'w')
outfile.write("Election Results\n")
outfile.write("-------------------------\n")
outfile.write(f"Total Votes: {total_votes}\n")
outfile.write(f"-------------------------\n")
for i in candidate_votes.items():
    outfile.write(f'{i[0]}: {round(candidate_percentages[i[0]],3)}% ({i[1]})\n')
outfile.write(f"-------------------------\n")
outfile.write(f"Winner: {winner}\n")
outfile.write("-------------------------\n")
outfile.close()
