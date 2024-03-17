
import json

# Load the data from 'pooltogether.json'
with open('FILENAME.json', 'r') as file:
    data = json.load(file)

# Convert the hexadecimal amounts to decimal and update the data
for entry in data:
    entry['amount'] = str(int(entry['amount'], 16))

# Save the updated data back to 'pooltogether.json'
with open('FILENAME.json', 'w') as file:
    json.dump(data, file, indent=2)

print("Conversion completed successfully.")
