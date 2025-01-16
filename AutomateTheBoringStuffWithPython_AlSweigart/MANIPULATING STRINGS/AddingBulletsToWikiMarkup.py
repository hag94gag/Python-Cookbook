
# Importing the necessary modules
import pyperclip

# Adding bullets to the text copied to the clipboard based on the new line
pragraph=pyperclip.paste()
npragraph=pragraph.split("\n")

# Adding the bullets to every line
for indx,chr in enumerate(npragraph):
    npragraph[indx]=(f"* {chr}")
    
#printing the new paragraph    
print("\n".join(npragraph))

#Copying the new paragraph to the clipboard   
pyperclip.copy("\n".join(npragraph))



        

