import re  # Importing the regular expressions module

# Sample text with typos
text = """
This  is a    sentence with multiple   spaces.
This is is an example of repeated words.
Wow!! That was amazing!!! But wait... Really???
"""

# Fix multiple spaces between words
text = re.sub(r"\s{2,}", " ", text)
# Explanation:
# \s{2,}  : Matches two or more consecutive whitespace characters
# " "     : Replaces the matched whitespace with a single space

# Fix accidentally repeated words (case insensitive)
text = re.sub(r"\b(\w+)\b\s+\b\1\b", r"\1", text, flags=re.IGNORECASE)
# Explanation:
# \b(\w+)\b  : Matches a whole word and captures it in a group (group 1)
# \s+        : Matches one or more spaces after the word
# \b\1\b     : Matches the same word (captured in group 1) again
# r"\1"      : Replaces the repeated words with just the first instance
# flags=re.IGNORECASE : Ensures the matching is case insensitive

# Fix excessive exclamation marks or other punctuation
text = re.sub(r"(!{2,})", "!", text)
# Explanation:
# !{2,} : Matches two or more consecutive exclamation marks
# "!"    : Replaces them with a single exclamation mark

text = re.sub(r"(\?{2,})", "?", text)
# Explanation:
# \?{2,} : Matches two or more consecutive question marks
# "?"     : Replaces them with a single question mark

text = re.sub(r"(\.{3,})", "...", text)
# Explanation:
# \.{3,} : Matches three or more consecutive dots (ellipses)
# "..."   : Replaces them with exactly three dots

# Print the cleaned text
print(text)

