# Import the random module to generate random numbers
import random 

# Dictionary containing states and their capitals
Countries = \
                {
                    "Alabama":           "Montgomery",
                    "Alaska":            "Juneau",
                    "Arizona":           "Phoenix",
                    "Arkansas":          "Little Rock",
                    "California":        "Sacramento",
                    "Colorado":          "Denver",
                    "Connecticut":       "Hartford",
                    "Delaware":          "Dover",
                    "Florida":           "Tallahassee",
                    "Georgia":           "Atlanta",
                    "Hawaii":            "Honolulu",
                    "Idaho":             "Boise",
                    "Illinois":          "Springfield",
                    "Indiana":           "Indianapolis",
                    "Iowa":              "Des Moines",
                    "Kansas":            "Topeka",
                    "Kentucky":          "Frankfort",
                    "Louisiana":         "Baton Rouge",
                    "Maine":             "Augusta",
                    "Maryland":          "Annapolis",
                    "Massachusetts":     "Boston",
                    "Michigan":          "Lansing",
                    "Minnesota":         "Saint Paul",
                    "Mississippi":       "Jackson",
                    "Missouri":          "Jefferson City",
                    "Montana":           "Helena",
                    "Nebraska":          "Lincoln",
                    "Nevada":            "Carson City",
                    "New Hampshire":     "Concord",
                    "New Jersey":        "Trenton",
                    "New Mexico":        "Santa Fe",
                    "New York":          "Albany",
                    "North Carolina":    "Raleigh",
                    "North Dakota":      "Bismarck",
                    "Ohio":              "Columbus",
                    "Oklahoma":          "Oklahoma City",
                    "Oregon":            "Salem",
                    "Pennsylvania":      "Harrisburg",
                    "Rhode Island":      "Providence",
                    "South Carolina":    "Columbia",
                    "South Dakota":      "Pierre",
                    "Tennessee":         "Nashville",
                    "Texas":             "Austin",
                    "Utah":              "Salt Lake City",
                    "Vermont":           "Montpelier",
                    "Virginia":          "Richmond",
                    "Washington":        "Olympia",
                    "West Virginia":     "Charleston",
                    "Wisconsin":         "Madison",
                    "Wyoming":           "Cheyenne"
                }

# Create a new dictionary with numerical keys and state-capital pairs as list values
CountriesDict = {}
for num, (con, cap) in enumerate(Countries.items()):
    CountriesDict[num + 1] = [con, cap]

# Initialize lists and variables to handle the question and answer process
RndEX = []  # Stores already selected random questions
RndQes = 0  # Stores the random question number
QizQes = 0  # Tracks the number of questions generated
Ans = []  # Stores the possible answers
cnt = 0  # Counter for the number of question sets created

# Loop to generate 36 sets of questions and answers
while cnt < 36:
    cnt += 1  # Increment the count of generated question sets
    RndQes = 0  # Reset random question number
    QizQes = 0  # Reset question counter
    RndEX.clear()  # Clear the list of previously selected questions
    
    # Open files to store questions and answers for each set
    with open(fr"C:\Users\DataCenter\Documents\QZ\Test{cnt}.txt", "w") as f:
        with open(fr"C:\Users\DataCenter\Documents\QZ\Answers{cnt}.txt", "w") as a:
            # Generate 50 questions per set
            while QizQes < 50:
                RndQes = random.randint(1, 50)  # Randomly select a question
                if RndQes not in RndEX:  # Ensure the question is unique
                    QizQes += 1  # Increment the question counter
                    RndEX.append(RndQes)  # Add question to the list of selected questions
                    # Write the question to the file
                    f.write(f"\n{QizQes} What is the Capital of {CountriesDict[RndQes][0]}\n")
                    # Prepare a list of answers with one correct and three random incorrect answers
                    Ans = [
                        CountriesDict[RndQes][1],
                        CountriesDict[random.randint(1, 50)][1],
                        CountriesDict[random.randint(1, 50)][1],
                        CountriesDict[random.randint(1, 50)][1]
                    ]
                    
                    # Shuffle the answers randomly
                    random.shuffle(Ans)
                    # Create a list of answers with labels (A, B, C, D)
                    LtrAns = [{"A": Ans[0]}, {"B": Ans[1]}, {"C": Ans[2]}, {"D": Ans[3]}]
                    
                    # Write the answer choices to the file and identify the correct one
                    for an in LtrAns:
                        for innk, innv in an.items():
                            f.write(f"{innk} {innv}")
                            if innv == CountriesDict[RndQes][1]:  # Identify the correct answer
                                Ltr = innk  # Store the letter of the correct answer
                        f.write("\n")
                    f.write("*" * 25)  # Add a separator line
                    # Write the correct answer to the answers file
                    a.write(f"{QizQes} {Ltr}\n")
                    a.write(f"{CountriesDict[RndQes][1]}\n")
                    a.write("*" * 25)
                    a.write("\n")
