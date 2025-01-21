import re

# Sample text containing sensitive information
text = """
John Doe's Social Security Number is 123-45-6789.
His credit card number is 1234-5678-9876-5432.
Another card number: 4321987612345678.
"""

# Patterns for SSNs and credit card numbers
ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b"
cc_pattern = r"\b\d{4}-?\d{4}-?\d{4}-?\d{4}\b"

# Replace sensitive information with placeholders
cleaned_text = re.sub(ssn_pattern, "[REDACTED-SSN]", text)
cleaned_text = re.sub(cc_pattern, "[REDACTED-CC]", cleaned_text)

# Print the cleaned text
print(cleaned_text)
