import os
import csv

csvfile = '.\\Resources\\budget_data.csv'

full_data = list()

with open(csvfile) as hshs:
    reader = csv.reader(hshs)
    for row in reader:
        full_data.append(row)


full_data_no_headers = full_data[1:]

no_months = len(full_data_no_headers)

net_total  = 0

for i in full_data_no_headers:
    net_total = net_total + int(i[1])

net_total

profs = [i[1] for i in full_data_no_headers]
delts = list()
ind_delts = dict()

for i in range(len(profs)-1):
    diff = int(profs[i+1]) - int(profs[i])
    delts.append(diff)
    ind_delts[i] = int(diff)

avg_ch = sum(delts)/len(delts)

full_sorted = sorted(full_data_no_headers, key=lambda x: x[1])

inc_mo, inc_amt = full_sorted[-1][0], full_sorted[-1][1]
dec_mo, dec_amt = full_sorted[0][0], full_sorted[0][1]

outfile = './analysis/Financial Analysis.txt'

out = open(outfile,'w')
out.write("Financial Analysis")
out.write("\n----------------------------")
out.write(f"\nTotal months: {no_months}")
out.write(f"\nTotal: ${net_total}")
out.write(f"\nAverage Change: ${round(avg_ch, 2)}")
out.write(f"\nGreatest Increase in Profits: {inc_mo} (${inc_amt})")
out.write(f"\nGreatest Decrease in Profits: {dec_mo} (${dec_amt})")
out.close()
