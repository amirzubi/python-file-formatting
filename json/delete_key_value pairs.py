# This script removes all fields from each entry in a JSON file except for "address" and "amount".

import json

# Load the JSON data from the file
with open('FILENAME.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Keep only "address" and "amount" for each entry
cleaned_data = [
    {"address": entry["address"], "amount": entry["amount"]}
    for entry in data
]

# Write the cleaned data back to the file or a new file
with open('FILENAMEjson', 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=2)

# Note: Replace 'path_to_your_json_file.json' and 'path_to_your_cleaned_json_file.json' 
# with the actual paths to your input and output files.