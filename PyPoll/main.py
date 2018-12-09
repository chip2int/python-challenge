import os
import csv
import statistics


csvpath = os.path.join('./', "election_data.csv")

voter_id = []
county = []
candidate = []
total_vote_count = 0
with open(csvpath, newline='') as cvsfile:
  csvreader = csv.reader(cvsfile, delimiter=',')

  csv_header = next(csvreader)

  for row in csvreader:
    county.append(row[1])
    candidate.append(row[2])


candidate_dict = {}

for x in set(candidate):
  candidate_dict[x] = 0

for x in candidate:
  candidate_dict[x] += 1

for x in candidate_dict:
  total_vote_count += candidate_dict[x]

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total_vote_count}")
print("-------------------------------")
for x in candidate_dict:
  print(f"{x}: {round((candidate_dict[x]/total_vote_count)*100)}% ({candidate_dict[x]})")
print("-------------------------------")
print(f"Winner: {max(candidate_dict, key=candidate_dict.get)}")
print("-------------------------------")


f = open("election_results.txt", "a")
f.write("-------------------------------\n")
f.write(f"Total Votes: {total_vote_count}\n")
f.write("-------------------------------\n")
for x in candidate_dict:
  f.write(f"{x}: {round((candidate_dict[x]/total_vote_count)*100)}% ({candidate_dict[x]})\n")
f.write("-------------------------------\n")
f.write(f"Winner: {max(candidate_dict, key=candidate_dict.get)}\n")
f.write("-------------------------------\n")

f.close()
