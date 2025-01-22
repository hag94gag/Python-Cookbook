import pyinputplus as pyip  # Import the pyinputplus library for input validation

# Infinite loop to repeatedly ask the user a question
while True:
    # Prompt the user with a question and expect a "yes" or "no" response
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)  # Ensures the input is either "yes" or "no"

    # If the user responds with "no," exit the loop
    if response == 'no':
        break  # Exit the loop when the user says "no"

# Print a friendly message after the loop ends
print('Thank you. Have a nice day.')






