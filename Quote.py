# Import RandomWords from the random_word module using the import keyword
from random_word import RandomWords
# Import quote from the quote module using the import keyword
from quote import quote
# Create an object for the RandomWords() to extract the words and store it in
# a variable.
randobj = RandomWords()
# Apply the get_random_word() function on the above object to get a random word
# and store it in another variable.
wrd = randobj.get_random_word()
# Print the above word obtained.
print("The result Keyword obtained = ", wrd)
# Pass the above word obtained and limit = 1 as the arguments to the quote()
# function to generate a quote at random.
# Set a limit to limit the number of quotes generated.
# Store it in another variable.
# The quote function provides a collection of dictionaries, each containing
# information about a certain quote.
rslt = quote(wrd, limit=1)
# Loop till the length of the above result dictionary using the for loop.
for itr in range(len(rslt)):
    # Print the corresponding quote.
    print("The result Quote obtained = ", rslt[itr]['quote'])
