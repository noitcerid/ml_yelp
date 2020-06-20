# Python program to convert 
# JSON file to CSV

import json 
import csv

# Gather file input/output
input_file_name = input('Please enter the name of the input file: ')

# Get file name to process
output_file_name = input('Please enter the name of the output file: ')


# Opening JSON file and loading the data into the variable data 
with open(input_file_name, 'r') as json_file:
	data = json.load(json_file)

file_data = data

# now we will open a file for writing 
data_file = open(output_file_name, 'w') 

# create the csv writer object 
csv_writer = csv.writer(data_file) 

# Row counter for keeping track of row count and outputting header
count = 0

for row in file_data:
	if count == 0: 

		# Writing headers of CSV file 
		header = row.keys()
		csv_writer.writerow(header) 

	# Writing data of CSV file 
	csv_writer.writerow(row.values())
	count += 1

data_file.close()

print("##### Results #####")
print('Input File: {}'.format(input_file_name))
print('Output File: {}'.format(output_file_name))
print('Script wrote {:,} rows to {}'.format(count, output_file_name))
