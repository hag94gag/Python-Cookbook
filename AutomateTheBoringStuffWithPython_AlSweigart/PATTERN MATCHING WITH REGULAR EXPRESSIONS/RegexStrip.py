import re  # Importing the regular expressions module

# Define a function to strip leading and trailing whitespace from a string using a regular expression
def regex_strip(text):
    # Use `re.sub` to replace leading (`^\s+`) and trailing (`\s+$`) whitespace with an empty string
    return re.sub(r'^\s+|\s+$', '', text)

# Example input string with leading and trailing whitespace
text = "  Hello, World!  "

# Call the `regex_strip` function to remove the whitespace
stripped_text = regex_strip(text)

# Print the stripped text
print(stripped_text)

