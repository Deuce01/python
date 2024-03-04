# Make a single variable to store the path of the file. This is a constant value.
# This value must be replaced with the file path from your own system in the example below.
givenFilename = "samplefile.txt"
# Open the file in read-only mode. In this case, we're simply reading the contents of the file.
with open(givenFilename, 'r') as givenfilecontent:
    # Iterate through the lines of the file using the For loop.
    print('The words in the given file : ')
    for gvnfileline in givenfilecontent:
      # Split the words of the line using the split() function and store them in a variable(it is of type list).
        gvnfilewords = gvnfileline.split()
        # Loop in the above list using another Nested For loop
        # and print all the contents of the list using the print() function.
        for words in gvnfilewords:
            print(words)
