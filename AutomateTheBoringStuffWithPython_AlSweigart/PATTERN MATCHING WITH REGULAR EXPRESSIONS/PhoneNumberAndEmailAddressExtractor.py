import pyperclip, re  # Importing the pyperclip module for clipboard operations and the re module for regular expressions

# Retrieve text from the clipboard
txt = pyperclip.paste()

# Define a regular expression to match Egyptian phone numbers (+20 format)
Phone = re.compile(r"\+20[-|.|' ']?\d[-|.|' ']?\d{4}[-|.|' ']?\d{4}")
# Explanation:
# \+20             : Matches the country code for Egypt (+20)
# [-|.|' ']?       : Matches an optional separator (-, ., or a space)
# \d               : Matches a single digit (area code or first digit of the number)
# [-|.|' ']?       : Matches an optional separator
# \d{4}            : Matches 4 consecutive digits (middle part of the phone number)
# [-|.|' ']?       : Matches an optional separator
# \d{4}            : Matches 4 consecutive digits (last part of the phone number)

# Define a regular expression to match email addresses
Email = re.compile(r"[\d\w]+@[\d\w]*[\.]{0,1}[\w]+\.[\w]{2,4}")
# Explanation:
# [\d\w]+          : Matches one or more alphanumeric characters (local part of the email)
# @                : Matches the "@" symbol
# [\d\w]*          : Matches zero or more alphanumeric characters (subdomain, if any)
# [\.]{0,1}        : Matches zero or one literal "." (optional subdomain separator)
# [\w]+            : Matches one or more word characters (domain name)
# \.               : Matches a literal dot separating the domain and TLD
# [\w]{2,4}        : Matches a TLD of 2 to 4 characters (e.g., com, org, edu)

# Search for all matches of either phone numbers or email addresses in the text
result = re.findall(f"{Email.pattern}|{Phone.pattern}", txt)

# Copy the results back to the clipboard
pyperclip.copy(result)


