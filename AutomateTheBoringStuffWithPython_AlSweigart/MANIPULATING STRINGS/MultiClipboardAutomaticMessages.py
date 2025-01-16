# Implement a multi-clipboard program that saves multiple strings.

# Importing the necessary modules
import sys
import pyperclip

# dictionary containing the messages
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}
# Checking if the key is entered
if len(sys.argv)<2:
    #requesting the user to enter the key
    print ("Enter the key")
else:
    #copying the message to the clipboard
    pyperclip.copy(TEXT[sys.argv[1]])







    
