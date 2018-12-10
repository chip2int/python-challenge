import csv
import os
import importlib
states = importlib.import_module('us_state_abbrev')


id = []
name = []
dob = []
ssn = []
state = []

with open('employee_data.csv') as csvFile:
  csvreader = csv.reader(csvFile)

  csv_header = next(csvreader)

  for row in csvreader:
    id.append(row[0])
    name.append(row[1])
    dob.append(row[2])
    ssn.append(row[3])
    state.append(row[4])

def parse_name(name):
  split_name = name.split(" ")
  return split_name[0]+","+split_name[1]

def parse_date(date):
  split_date = date.split('-')
  return split_date[1] + "/" + split_date[2]+"/"+split_date[0]

def parse_state(state):
  return states.us_state_abbrev[state]

def parse_ssn(ssn):
  split_ssn = ssn.split('-')
  return '***-**-'+split_ssn[2]

name = [parse_name(i) for i in name]
dob = [parse_date(i) for i in dob]
state = [parse_state(i) for i in state]
ssn = [parse_ssn(i) for i in ssn]

new_entries = zip(id, name, dob, ssn, state)

output_file = os.path.join("output.csv")

with open(output_file, "w", newline="") as datafile:
  writer = csv.writer(datafile)
  writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
  writer.writerows(new_entries)

