import csv
import json

# Define the input and output file paths
input_file = 'BRCA_data.tsv'
output_file = 'fixtures/BRCA_data_converted.json' 

# Read the TSV file and convert it to a list of dictionaries
data = []
with open(input_file, 'r', newline='', encoding='utf-8') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    for row in reader:
        data.append(row)

# Write the data to a JSON file
with open(output_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)