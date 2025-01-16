# Takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
def printTable(ls:list[str]) -> None: # The function takes a list of lists of strings and returns nothing
    # loop to iterate through the list
    for line in ls:
        # loop to iterate through the strings in the list
        for word in line:
            print(word.rjust(10),end="") # printing the word right justified
        print() # printing a new line


# Testing the function
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)