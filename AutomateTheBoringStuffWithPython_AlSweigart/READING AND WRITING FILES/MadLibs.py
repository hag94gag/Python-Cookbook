import re

def mad_libs(filename):
    try:
        # Step 1: Read the input file
        with open(filename, 'r') as file:
            content = file.read()

        # Step 2: Find placeholders (ADJECTIVE, NOUN, VERB, ADVERB)
        placeholders = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', content)

        # Step 3: Prompt the user for each placeholder
        for placeholder in placeholders:
            user_input = input(f"Enter a {placeholder.lower()}: ")
            # Replace only the first occurrence of the placeholder
            content = content.replace(placeholder, user_input, 1)

        # Step 4: Display the completed Mad Libs story
        print("\nHere is your completed Mad Libs story:\n")
        print(content)

        # Step 5: Optionally save the result to a new file
        save_choice = input("\nWould you like to save this story to a file? (yes/no): ").strip().lower()
        if save_choice in ('yes', 'y'):
            output_filename = input("Enter the output filename (e.g., completed_mad_libs.txt): ")
            with open(output_filename, 'w') as output_file:
                output_file.write(content)
            print(f"Your story has been saved to {output_filename}.")
        else:
            print("Your story was not saved.")

    except FileNotFoundError:
        print(f"The file '{filename}' does not exist. Please check the file path and try again.")

# Example usage
input_file = input("Enter the name of the text file with the Mad Libs template: ")
mad_libs(input_file)
