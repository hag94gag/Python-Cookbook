# Big Latin rules:
    # If a word starts with a vowel (a, e, i, o, u), add "yay" to the end of the word.
    # Example: apple → appleyay
    # If a word starts with a consonant, move all the consonants at the start of the word to the end, and add "ay".
    # Example: hello → ellohay
    # Words are separated by spaces, and punctuation should be preserved.

# a function that takes a string and returns the Pig Latin version of it.
def PigLatin (txt:str):
    vowels="aeiou" #vowels
    Ntxt=txt.split(" ") #splitting the text into words
    Vtxt="" #variable to store the Pig Latin version of the text
    Ctxt="" #variable to store the consonants
    # loop to check the first letter of each word
    for i in Ntxt:
        #checking if the first letter is a vowel
        if i[0] in vowels:
            #adding yay to the end of the word
            Vtxt+=i+"yay "
        # checking if the first letter is a consonant
        elif i[0] not in vowels:
            # loop to check the consonants at the start of the word
            for x in i:
                # checking if the letter is a vowel
                if x in vowels:
                    #breaking the loop if the letter is a vowel
                    break
                # adding the consonants to the variable Ctxt
                else:
                    Ctxt+=x
            # adding the consonants and ay to the end of the word
            Vtxt+=i[len(Ctxt):]+Ctxt+"yay "
            
            
    # returning the Pig Latin version of the text
    return Vtxt
    
    
# testing the function
print (PigLatin("""A Short Progam: Pig Latin
Pig Latin is a silly made-up language that alters English words. If a word begins with a vowel, the word yay is
added to the end of it. If a word begins with a consonant or consonant cluster (like ch or gr), that consonant
or cluster is moved to the end of the word followed by ay.
"""))