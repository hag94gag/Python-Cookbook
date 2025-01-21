import re  # Import the `re` module for working with regular expressions

# Input text containing dates in different formats
txt = "In 12/03/2018 John dead and in  20-4-2048 he came back from the death"

# Define a regular expression pattern to match dates in the formats `dd/mm/yyyy`, `dd-mm-yyyy`, etc.
Pattern = re.compile(r"(\d{1,2})[\\/-](\d{1,2})[\\/-](\d{4})")
# Explanation:
# (\d{1,2})   : Captures the day or month (1 or 2 digits)
# [\\/-]      : Matches a literal `/`, `-`, or `\` as a separator
# (\d{1,2})   : Captures the month or day (1 or 2 digits)
# [\\/-]      : Matches a literal `/`, `-`, or `\` as a separator
# (\d{4})     : Captures the year (exactly 4 digits)

# Search for the first match of the pattern in the input text
result = re.search(Pattern, txt)

# If a match is found
if result:
    # Check if the year (group 3) has more characters than the day/month (group 1)
    if len(result.group(3)) > len(result.group(1)):
        # If true, reformat the date to the format `yyyy-mm-dd`
        newDate = re.sub(Pattern, r"\3-\2-\1", txt)
    else:
        # Otherwise, keep the original order as `dd-mm-yyyy`
        newDate = re.sub(Pattern, r"\1-\2-\3", txt)

# Print the modified text with the reformatted date
print(newDate)
