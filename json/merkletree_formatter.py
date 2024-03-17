import json

# Load your original JSON data
with open('FILENAME.json', 'r') as file:
    original_data = json.load(file)

# Transform the data
transformed_data = [
    {"address": address, "amount": details["amount"]}
    for address, details in original_data.items()
]

# Write the transformed data back to the file
with open('FILENAME.json', 'w') as file:
    json.dump(transformed_data, file, indent=4)

print("The file has been updated with the new structure.")
