
x = 0

# Create a file to output new results
output_file = open('data/yelp_academic_dataset_review_array.json', 'w')

# Write beginning of array
output_file.write('[')

with open('data/yelp_academic_dataset_review.json', 'r') as f:
    # Append a comma prior to the first { of every except the first line
    for line in f:
        if x == 0:
            output_file.write(line)
        else:
            output_file.write(',' + line)
        
        x += 1

# Write end of json array
output_file.write(']')


print('Script wrote ' + str(x) + ' lines.')
