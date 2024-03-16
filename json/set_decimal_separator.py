import json

def format_amount(amount):
    amount = str(amount)
    # Change the number 18 to the count of characters from right where a decimal seperater should be placed
    if len(amount) > 18:
        integer_part = amount[:-18]
        decimal_part = amount[-18:]
        formatted_amount = f"{integer_part}.{decimal_part}"
        return formatted_amount

# Path to your JSON file
file_path = 'FILENAME.json'

# Load the JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

# Format the amounts in the data
for entry in data:
    if 'amount' in entry:
        entry['amount'] = format_amount(entry['amount'])

# Overwrite the original file with formatted data
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Amounts have been formatted and saved.")
