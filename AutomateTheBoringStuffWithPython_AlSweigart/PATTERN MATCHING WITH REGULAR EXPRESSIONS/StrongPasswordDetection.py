import re  # Import the `re` module for working with regular expressions

# Input text to test for password strength
txt = "Qwe@123"

# Define a regular expression to check for a strong password
SPass = re.compile(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_\\|])")
# Explanation:
# (?=.*[A-Z])          : Positive lookahead to ensure at least one uppercase letter (A-Z)
# (?=.*[a-z])          : Positive lookahead to ensure at least one lowercase letter (a-z)
# (?=.*\d)             : Positive lookahead to ensure at least one digit (0-9)
# (?=.*[!@#$%^&*()_\\|]): Positive lookahead to ensure at least one special character from the specified set

# Check if the password meets the "strong password" criteria
if SPass.search(txt):
    print("Strong password")  # Print this if all criteria are met
else:
    print("Weak password")  # Print this if any criteria are not met

