import re

# Input string containing dates in different formats
txt = "In 12/03/2018 John died and in 20-4-2048 he came back from the death"

# Compile a regex pattern to match dates in the formats DD/MM/YYYY, DD-MM-YYYY, or similar
Pattern = re.compile(r"(\d{1,2})[\\/-](\d{1,2})[\\/-](\d{4})")

# Search the input text for the first occurrence of a date matching the pattern
result = re.search(Pattern, txt)

# Check if a date was found in the text
if result:
    # If the year (group 3) is longer than the day (group 1), assume the desired format is YYYY-MM-DD
    if len(result.group(3)) > len(result.group(1)):
        # Replace all matched dates with the format YYYY-MM-DD
        newDate = re.sub(Pattern, r"\3-\2-\1", txt)
    else:
        # Otherwise, keep the original format (DD-MM-YYYY)
        newDate = re.sub(Pattern, r"\1-\2-\3", txt)

# Print the modified text with reformatted dates
print(newDate)
