import csv
from pathlib import Path

def get_file_len(fname):
    print('Getting total rows in file...')
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Get file names to process
file_name = input('Please enter the name of the file to extract data from: ')
file_name_no_extension = str(Path(file_name).with_suffix(''))
file_name_training = file_name_no_extension + '_training.csv'
file_name_prediction = file_name_no_extension + '_prediction.csv'

# Get sample size from user
training_size = int(input('How many training samples would you like to extract? '))

# Get prediction size from user
prediction_size = int(input('How many prediction samples would you like to extract? '))

total_samples = training_size + prediction_size
valid_parameters = True
file_row_count = get_file_len(file_name)

# Check inputs
if total_samples > file_row_count:
    print('ERROR: Unable to process: Total samples requested exceed total file length ({:,} rows)'.format(file_row_count))
    valid_parameters = False

# Check to ensure we have at least one row for prediction
if training_size >= file_row_count - 1:
    print('ERROR: Training size exceeds allowable limits. Max training size is: {:,}'.format(file_row_count-1))
    valid_parameters = False


# Process files
if valid_parameters == True:
    print('Generating files...')
    training_data = open(file_name_training, 'w')
    prediction_data = open(file_name_prediction, 'w')

    x = 0
    # import file
    with open(file_name, 'r') as input_file:
        header_row = input_file.readline()
        training_data.writelines(header_row)
        prediction_data.writelines(header_row)
        while x <= total_samples:
            # Skip header row
            if x == 0:
                x += 1

            # Output training data
            print('\nProcessing training data...')
            while x <= training_size:
                if x % (training_size / 10) == 0:
                    print('Completed {:.0%}'.format(x / training_size))
                training_data.writelines(input_file.readline())
                x += 1
            print('Training data complete!')

            # Output prediction data
            prediction_iter = 1
            print('\nProcessing prediction data...')
            while x <= total_samples:
                if prediction_iter % (prediction_size / 10) == 0:
                    print('Completed {:.0%}'.format(prediction_iter / prediction_size))
                prediction_data.writelines(input_file.readline())
                x += 1
                prediction_iter += 1
            print('Prediction data complete!')

    training_data.close()
    prediction_data.close()

    print("\n##### Results #####")
    print('Input File: {}'.format(file_name))
    print('Output Files: ')
    print('\t{0} ({1:,}) rows'.format(file_name_training, training_size))
    print('\t{0} ({1:,}) rows'.format(file_name_prediction, prediction_size))
    print('Script wrote a total of {:,} rows to output files'.format(x - 1))
else:
    print('\nERROR: Unable to process... check input parameters and try again.')