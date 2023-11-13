import os
import csv

# create file path to read csv file
csvfile = os.path.join(".","Resources", "budget_data.csv")

full_data = list()

with open(csvfile) as hshs:
    reader = csv.reader(hshs)

    # for each row in the input file, append it to full_data (list)
    for row in reader:
        full_data.append(row)


# remove header from rows, but store in a different variable
full_data_no_headers = full_data[1:]  

# number of months is equal to length of this data 
no_months = len(full_data_no_headers)

# initialize net_total
net_total  = 0

# for each row, add the value to net_total
for i in full_data_no_headers:
    net_total = net_total + int(i[1])

# get a list of just the values from the full_data
profs = [i[1] for i in full_data_no_headers]

# initialize list for the changes (deltas) from month to month
delts = list()
ind_delts = dict()

# for each value in the profits,
# iterate through the months, get the difference between
# the current month and the next month, and append it
# to delts (list), and add it to dictionary ind_delts
# with key i (the number/index of the month in profs,
# which would follow the index in full_data_no_headers)
for i in range(len(profs)-1):
    diff = int(profs[i+1]) - int(profs[i])
    delts.append(diff)
    ind_delts[i] = int(diff)

# find the average change from month to month
avg_ch = sum(delts)/len(delts)

# sort the dictionary by value (profits) in ascending order
full_sorted = sorted(full_data_no_headers, key=lambda x: x[1])

# get the month with the greatest profit (increase), get the value of greatest profit (increase)
inc_mo = full_sorted[-1][0]
inc_amt = full_sorted[-1][1]

# get the month with the greatest decrease, get the value of the greatest lost (decrease)
dec_mo  = full_sorted[0][0], 
dec_amt = full_sorted[0][1]

# outfile process
outfile = os.path.join(".", "analysis", "Financial Analysis.txt")

out = open(outfile,'w')

out.write("Financial Analysis")
out.write("\n----------------------------")
out.write(f"\nTotal months: {no_months}")
out.write(f"\nTotal: ${net_total}")
out.write(f"\nAverage Change: ${round(avg_ch, 2)}")
out.write(f"\nGreatest Increase in Profits: {inc_mo} (${inc_amt})")
out.write(f"\nGreatest Decrease in Profits: {dec_mo} (${dec_amt})")

out.close()
