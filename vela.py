
import re
from collections import Counter

# Function to read chat log from a file


def read_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chat_log = file.readlines()
    return chat_log


# Path to the local text file
file_path = ''

# Read the chat log from the file
chat_log = read_chat_log(file_path)

# Regular expression to remove timestamps and everything after the colon
pattern = re.compile(r'\[.*?\] ~?\s*(.*?):.*')

# Extract names using the regular expression
names = [match.group(1) for line in chat_log if (match := pattern.match(line))]

# Count the frequency of each unique name
name_counts = Counter(names)

# Arrange names in order of messages sent
sorted_names = sorted(name_counts.items(), key=lambda x: x[1], reverse=True)

# Print the sorted names along with their counts
for name, count in sorted_names:
    print(f"{name}: {count}")

# Print the total number of unique names
print(f"Total unique names: {len(sorted_names)}")
