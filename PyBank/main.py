import os
import csv
import statistics

dates = []
profits_losses = []

csvpath = os.path.join('./', "budget_data.csv")

with open(csvpath, newline='') as cvsfile:
  csvreader = csv.reader(cvsfile, delimiter=',')

  csv_header = next(csvreader)

  for row in csvreader:
    dates.append(row[0])
    profits_losses.append(row[1])

profits_losses = list(map(int, profits_losses))

change_list = []
prev = profits_losses[0]
for element in profits_losses[1:]:
  change_list.append(element - prev)
  prev = element


average_change = round(statistics.mean(change_list))

max_change = max(change_list)
min_change = min(change_list)
max_change_index = change_list.index(max_change)
min_change_index = change_list.index(min_change)


print("Financial Analysis")
print("--------------------------------")
print(f"Number of entries: {len(dates)}")
print(f"Average Change: {average_change}")
print(f"Total: ${sum(profits_losses)}")
print(f"Greatest Increase in Profits: {dates[max_change_index + 1]} (${max_change})")
print(f"Greatest Decrease in Profits: {dates[min_change_index + 1]} (${min_change})")


