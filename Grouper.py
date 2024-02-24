# Import the defaultdict from collections using the import keyword.

from collections import defaultdict
# Give the list of strings as static input and store it in a variable.
gvnstrnglist = ['ehlo', 'this', 'is', 'olhe', 'helo', 'si', 'btechgeeks']
# The defaultdict method is used to construct a dictionary
# corresponding to a key that contains word characters.
# The list argument is used to generate key-value list pairs.
grpwords = defaultdict(list)

# Loop over the list of strings using For loop.
for strngword in gvnstrnglist:
    # The str method on sorted(word) returns a list of keys
    # that include the alphabets of words.
    # Append the word using append(word) joins together words that are related.
    grpwords[str(sorted(strngword))].append(strngword)

# Get all the values of the defaultdict using the values() function.
simipairs = list(grpwords.values())
# Print the defaultdict.
print('The group of words which are similar in given list of strings ',
      gvnstrnglist, 'is :')
print(simipairs)
