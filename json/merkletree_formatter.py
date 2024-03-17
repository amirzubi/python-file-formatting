import json

# Load your original JSON data
with open('FILENAME.json', 'r') as file:
    original_data = json.load(file)

# Transform the data
transformed_data = []
for item in original_data:
    for address, details in item.items():
        transformed_data.append({
            "address": address,
            "amount": int(details["amount"], 16)  # Convert hex to decimal
        })

# Write the transformed data back to the file
with open('FILENAME.json', 'w') as file:
    json.dump(transformed_data, file, indent=4)

print("The file has been updated with the new structure.")
