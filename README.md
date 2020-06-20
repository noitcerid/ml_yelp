# JSON to CSV Conversion Tools

This is a small set of scripts that modify the original files from the yelp academic data set in order to make them easier to process. The original data set comes with a comma-delimited list of JSON objects, but technically isn't a JSON-compatible format (which complicates parsing). The goal of this work was to convert these objects ultimately into an importable CSV file for doing some machine learning.

## Scripts

### yelp_to_json_array.py
This script converts the original files into a JSON array to make it a complete (valid) JSON document.

### json_to_csv.py
This script converts a JSON array to a CSV file. This was the first iteration of the converter and works fine for smaller data sets, but python crashed when I got to > 4.5GB files or so (on my 16GB RAM linux laptop), so this is non-optimal for processing very large files.

### json_to_csv_iter.py
This script iteratively parses through the JSON array file, helping to optimize memory usage. In this case, I manually built the headers (only the review file was too large to process with json_to_csv.py). Hoping to enhance that with reading out the first record, writing a header, and then being able to pass whatever data is processed, rather than manually building the output.

### csv_sample.py
This script takes an input file and outputs two files, one with "_training" appended, and the other with "_prediction" in order to simplify using subsets of the data. Note that it only reads from the beginning of the file, so if you want a more random sample from the large file, you need to process that in your ML tool (Orange has a random sample option).